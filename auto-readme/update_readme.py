import sys
import re
import asyncio
import pickle


from typing import List, Dict
from git import Repo
from crawler import upsert_problems, get_problems

# 관리할 폴더
PLATFORMS = ["baekjoon", "programmers"]  # , "softeer"]
# README 작성 관련
MD_NAME = "test.md"
MD_HEADER = {
    "baekjoon": "Baekjoon 문제 풀이 내역",
    "programmers": "Programmers 문제 풀이 내역",
    "softeer": "Softeer 문제 풀이 내역"
}
MD_DIFFICULTY = {
    # Programmers
    "LV1": "⭐☆☆☆☆",
    "LV2": "⭐⭐☆☆☆",
    "LV3": "⭐⭐⭐☆☆",
    "LV4": "⭐⭐⭐⭐☆",
    "LV5": "⭐⭐⭐⭐⭐",
    # Softeer
    "1": "⭐☆☆☆☆",
    "2": "⭐⭐☆☆☆",
    "3": "⭐⭐⭐☆☆",
    "4": "⭐⭐⭐⭐☆",
    "5": "⭐⭐⭐⭐⭐",
    # Baekjoon
    "B5": "![티어](/auto-readme/src/1.svg)",
    "B4": "![티어](/auto-readme/src/2.svg)",
    "B3": "![티어](/auto-readme/src/3.svg)",
    "B2": "![티어](/auto-readme/src/4.svg)",
    "B1": "![티어](/auto-readme/src/5.svg)",
    "S5": "![티어](/auto-readme/src/6.svg)",
    "S4": "![티어](/auto-readme/src/7.svg)",
    "S3": "![티어](/auto-readme/src/8.svg)",
    "S2": "![티어](/auto-readme/src/9.svg)",
    "S1": "![티어](/auto-readme/src/10.svg)",
    "G5": "![티어](/auto-readme/src/11.svg)",
    "G4": "![티어](/auto-readme/src/12.svg)",
    "G3": "![티어](/auto-readme/src/13.svg)",
    "G2": "![티어](/auto-readme/src/14.svg)",
    "G1": "![티어](/auto-readme/src/15.svg)",
    "P5": "![티어](/auto-readme/src/16.svg)",
    "P4": "![티어](/auto-readme/src/17.svg)",
    "P3": "![티어](/auto-readme/src/18.svg)",
    "P2": "![티어](/auto-readme/src/19.svg)",
    "P1": "![티어](/auto-readme/src/20.svg)",
    "D5": "![티어](/auto-readme/src/21.svg)",
    "D4": "![티어](/auto-readme/src/22.svg)",
    "D3": "![티어](/auto-readme/src/23.svg)",
    "D2": "![티어](/auto-readme/src/24.svg)",
    "D1": "![티어](/auto-readme/src/25.svg)",
    "R5": "![티어](/auto-readme/src/26.svg)",
    "R4": "![티어](/auto-readme/src/27.svg)",
    "R3": "![티어](/auto-readme/src/28.svg)",
    "R2": "![티어](/auto-readme/src/29.svg)",
    "R1": "![티어](/auto-readme/src/30.svg)",
}
# 파일명 사용 불가로 사용할 수 없는 문자들
MD_S_CHARS = {
    "＼": "\\",
    "／": "/",
    "：": ":",
    "＊": "*",
    "？": "?",
    "＂": '"',
    "＜": "<",
    "＞": ">",
    "｜": "|"
}


# git 활용
GIT_REPO = Repo.init("../")
GIT_BRANCH = GIT_REPO.active_branch
GIT_BASE_DIR = f"https://github.com/woodywarhol9/algorithm-practice/blob/{GIT_REPO.head.commit}"


class FileInfo:
    def __init__(self, path: str, platform: str, is_sol: str, dt: str, difficulty: str, *title: List[str]):
        """
        파일 정보 저장
        - path : programmers/solved/파일명.py
        - platform : programmers
        - is_sol : solved/retry
        - dt : 최초 커밋 날짜
        - difficulty : 난이도
        - title : 파일명 -> 실제 문제명 + 하이퍼링크
        """
        self.path = path
        self.platform = platform
        self.is_sol = is_sol
        self.dt = dt
        self.difficulty = difficulty
        self.title = "".join(*title)


def get_dt(path: str) -> str:
    """
    정렬 기준으로 사용할 최종 커밋 날짜 확인
    """
    dt = GIT_REPO.git.log("--follow", "--pretty=%cd",
                          "--date=format:%Y-%m-%d", path).split("\n")[0]
    return dt


def get_FileInfos_by_platform(file_paths: List[str]) -> Dict[str, List[FileInfo]]:
    """"
    플랫폼 별 파일 정보 반환
    - {"baekjoon" : ["1001", "1002"], "programmers" : ["문제 1", "문제 2"]}
    """
    file_infos = {}
    for file_path in file_paths:
        # 문제 풀이 파일 정보만 저장하기
        if file_path[-2:] == ".py":
            platform, is_sol, *file = file_path.split("/")
            if platform not in file_infos:
                file_infos[platform] = []
            file = file[-1]
            dt = get_dt(file_path)
            # 특수 문자로 인해 변경해서 저장한 파일명 다시 되돌리기
            for s_char in MD_S_CHARS:
                file = file.replace(s_char, MD_S_CHARS[s_char])
            file_infos[platform].append(
                FileInfo(file_path, platform, is_sol, dt, file[:-3].split("_")[0], file[:-3].split("_")[1:]))
    return file_infos


def modify_titles(file_infos: List[FileInfo], problem_infos: Dict[str, List[str]]):
    """
    문제 이름 수정 및 하이퍼링크 적용
    - 실제 문제 이름과 달리 파일명엔 공백이 없음 -> 크롤링해서 받아온 이름 활용
    - 불필요한 단어 제거 : [1차], [2021년 ~~] 등의 패턴 제거
    """
    title_dict = {problem_key.replace(
        " ", ""): problem_info[1] for problem_key, problem_info in problem_infos.items()}
    url_dict = {problem_key.replace(
        " ", ""): problem_info[2] for problem_key, problem_info in problem_infos.items()}
    for file_info in file_infos:
        # 불필요한 단어 제거
        if file_info.platform == "baekjoon":
            file_info.title = re.sub(r"[^\d]", "", file_info.title)
        file_info.title, url = re.sub(
            r"^\[.+]", "", title_dict[f"{file_info.platform}/{file_info.title}"]), url_dict[f"{file_info.platform}/{file_info.title}"]
        file_info.title = file_info.title.lstrip()
        # 하이퍼 링크 추가
        file_info.title = f"[{file_info.title}]({url})"


def cnt_lines(platform: str, md_name: str) -> int:
    with open(f"../{platform}/{md_name}", "r", encoding="UTF-8") as readme:
        return (len(readme.readlines()) - 3)


def get_lines(file_infos: List[FileInfo], start_idx: int) -> str:
    """
    문제 풀이 정보 저장
    """
    file_infos.sort(key=lambda x: (x.dt))
    md_lines = []
    for idx, file_info in enumerate(file_infos):
        sol = '✔️' if file_info.is_sol == "solved" else '❌'
        md_lines.append(
            f"|{idx+1+start_idx}|{file_info.dt}|{file_info.title}|[Link]({GIT_BASE_DIR}/{file_info.path})|{MD_DIFFICULTY[file_info.difficulty.upper()]}|{sol}|")
    # 마크다운 테이블 형식
    return "\n".join(md_lines[::-1])  # 가장 최근에 푼 문제가 가장 상위에 작성되도록


def update_readme(md_lines: str, platform: str):
    """
    플랫폼 별 README 파일 업데이트
    """
    with open(f"../{platform}/{MD_NAME}", "r+", encoding="UTF-8") as readme:
        lines = readme.readlines()
        header, prev_lines = lines[:3], lines[3:]
        # 제일 첫 줄로 이동
        readme.seek(0)
        readme.writelines(header)
        readme.writelines(md_lines)
        readme.write("\n")
        readme.writelines(prev_lines)


def concat_readme(platforms: List[str]):
    """
    전체 README 파일 작성
    """
    with open(f"../{MD_NAME}", "w", encoding="UTF-8") as main_readme:
        # 헤더 내용
        main_readme.write("# Problem Solving" + "\n")
        main_readme.write("알고리즘 문제 풀이 내역을 업로드합니다." + "\n")
        main_readme.write("### 사이트 별 풀이 확인" + "\n")
        # 목차 작성
        for platform in platforms:
            main_readme.write(
                f"- [{platform.capitalize()}](#{'-'.join(MD_HEADER[platform].split())})" + "\n")
        main_readme.write("---" + "\n")
        # 각 플랫폼 별 README 파일 불러와서 병합하기
        for platform in platforms:
            with open(f"../{platform}/{MD_NAME}", "r", encoding="UTF-8") as readme:
                main_readme.write(readme.read() + "\n")
                main_readme.write("---" + "\n")


def run_main() -> bool:
    """
    README 업데이트 진행
    - 성공 시 True, 실패 시 False 반환
    """
    # 윈도우 10 문제 해결
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # 새로 Commit된 File만 확인
    file_paths = GIT_REPO.git.diff(
         [f"origin/{GIT_BRANCH}..{GIT_BRANCH}"], name_only=True)
    file_paths = file_paths.split("\n")
    # # 문제 풀이와 관련된 파일만 불러오기
    file_paths = [file_path for file_path in file_paths if file_path.split(
        "/")[0] in PLATFORMS]
    file_infos_platform = get_FileInfos_by_platform(file_paths)
    # 커밋된 파일이 문제 풀이랑 상관 없는 경우
    if not file_infos_platform:
        return False
    print("새로 Commit된 File 정보 받아옴")
    problems = asyncio.run(get_problems({platform: [
                        file_info.title for file_info in file_infos] for platform, file_infos in file_infos_platform.items()}))
    print("크롤링 완료")
    problem_infos = upsert_problems(problems)
    print("문제 정보 업데이트 완료")
    with open("test", "rb") as file:
        problem_infos = pickle.load(file)
    modify_titles(sum(file_infos_platform.values(), []), problem_infos)
    print("문제 이름 수정 완료")
    # 각 플랫폼 별 풀이 내역 수정하기
    for platform, file_infos in file_infos_platform.items():
        start_idx = cnt_lines(platform, MD_NAME)  # 신규 문제 idx 확인
        md_lines = get_lines(file_infos, start_idx)
        update_readme(md_lines, platform)
        print(f"{platform} README 수정 완료")
    # 전체 풀이 내역 작성하기
    concat_readme(PLATFORMS)
    print("전체 README 수정 완료")
    return True


if __name__ == "__main__":
    # README 업데이트 성공 여부 확인
    condition = run_main()
    # Github Actions의 실행 조건 전달
    print(f"DO_UPDATE={condition}")