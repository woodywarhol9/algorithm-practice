import os
import re
from typing import List, Dict, Tuple
from git import Repo
from crawler import *

# 관리할 폴더
PLATFORMS = ["baekjoon", "programmers"] #, "softeer"]
# README 작성 관련
MD_HEADER = {
    "baekjoon": "Baekjoon 문제 풀이 내역",
    "programmers": "Programmers 문제 풀이 내역",
    "softeer": "Softeer 문제 풀이 내역"
}
MD_TABLE = """\
| \# | Date | Problem | Solution | Difficulty | Solved |
| :----: | :------: | :---------------: | :-----: | :------: | :-------: |\
"""
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
    "B5": "![티어](./src/1.svg)",
    "B4": "![티어](./src/2.svg)",
    "B3": "![티어](./src/3.svg)",
    "B2": "![티어](./src/4.svg)",
    "B1": "![티어](./src/5.svg)",
    "S5": "![티어](./src/6.svg)",
    "S4": "![티어](./src/7.svg)",
    "S3": "![티어](./src/8.svg)",
    "S2": "![티어](./src/9.svg)",
    "S1": "![티어](./src/10.svg)",
    "G4": "![티어](./src/12.svg)",
    "G5": "![티어](./src/11.svg)",
    "G2": "![티어](./src/14.svg)",
    "G3": "![티어](./src/13.svg)",
    "P5": "![티어](./src/16.svg)",
    "G1": "![티어](./src/15.svg)",
    "P3": "![티어](./src/18.svg)",
    "P4": "![티어](./src/17.svg)",
    "P1": "![티어](./src/20.svg)",
    "P2": "![티어](./src/19.svg)",
    "D4": "![티어](./src/22.svg)",
    "D5": "![티어](./src/21.svg)",
    "D2": "![티어](./src/24.svg)",
    "D3": "![티어](./src/23.svg)",
    "R5": "![티어](./src/26.svg)",
    "D1": "![티어](./src/25.svg)",
    "R3": "![티어](./src/28.svg)",
    "R4": "![티어](./src/27.svg)",
    "R1": "![티어](./src/30.svg)",
    "R2": "![티어](./src/29.svg)",
}
# 파일명 사용 불가로 사용할 수 없는 문자들
MD_S_CHARS = {
    "＼" : "\\",
    "／" : "/",
    "：" : ":",
    "＊" : "*",
    "？" : "?",
    "＂" : '"',
    "＜" : "<",
    "＞" : ">",
    "｜" : "|"
    }

# git 활용
GIT_REPO = Repo.init("../")
GIT_BRANCH = GIT_REPO.active_branch
GIT_BASE_DIR = f"https://github.com/woodywarhol9/algorithm-practice/blob/{GIT_REPO.head.commit}/"


class FileInfo:
    def __init__(self, path: str, platform: str, is_sol: str, dt: str, difficulty : str, *title: List[str]):
        """
        파일 정보 저장
        - path : programmers/solved/파일명.py
        - platform : programmers
        - is_sol : solved/retry
        - title : 파일명 -> 실제 사이트에 적힌 파일명
        - dt : 최초 커밋 날짜
        """
        self.path = path
        self.platform = platform
        self.is_sol = is_sol
        self.title = "".join(*title)
        self.dt = dt
        self.difficulty = difficulty


def get_dt(path: str) -> str:
    """
    정렬 기준으로 사용할 최초 커밋 날짜 확인
    """
    dt = GIT_REPO.git.log("--follow", "--pretty=%cd",
                      "--date=format:%Y-%m-%d", path).split("\n")[-1]
    return dt


def get_FileInfos_by_platform(platforms: List[str]) -> Dict[str, List[FileInfo]]:
    """"
    플랫폼 별 파일 정보 반환
    - {"baekjoon" : ["1001", "1002"], "programmers" : ["문제 1", "문제 2"]}
    """
    file_infos = {}
    for platform in platforms:
        file_infos[platform] = []
        for (root, dirs, files) in os.walk(os.path.join("../", platform)):
            root = re.split(r"[/\\]", root[2:])  # "\" : 윈도우 운영체제
            for file in files:
                if file[-2:] == "py":
                    path =  f"./{GIT_BRANCH}{'/'.join([*root, file])}"
                    dt = get_dt(path)
                    # 특수 문자로 인해 변경해서 저장한 파일명 다시 되돌리기
                    for s_char in MD_S_CHARS:
                        file = file.replace(s_char, MD_S_CHARS[s_char])
                    file_infos[platform].append(
                        FileInfo(path, root[0], root[1], dt, file[:-3].split("_")[0], file[:-3].split("_")[1:]))
    return file_infos

def modify_title(file_infos: Tuple[FileInfo], problems: List[Problem]):
    """
    문제 이름 수정
    - 실제 문제 이름과 달리 파일명엔 공백이 없음 -> 크롤링해서 받아온 이름 활용
    - 불필요한 단어 제거 : [1차], [2021년 ~~] 등의 패턴 제거
    """
    title_dict = {"".join(problem.title) : problem.title for problem in problems}
    for file_info in file_infos:
        file_info.title = re.sub(r"^\[.+]$" ,"", title_dict[file_info.title])
        print(file_info.title)


def get_lines(file_infos: List[FileInfo]) -> str:
    """
    문제 풀이 정보 저장
    """
    file_infos.sort(key=lambda x: (x.dt))
    md_lines = []
    for idx, file_info in enumerate(file_infos):
        sol = '✔️' if file_info.is_sol == "solved" else '❌'
        md_lines.append(
            f"{idx+1}|{file_info.dt}|{file_info.title}|[Link]({BASE_DIR}{file_info.path})|{MD_DIFFICULTY[file_info.difficulty.upper()]}|{sol}")
    # 마크다운 테이블 형식
    md_lines.append(MD_TABLE)
    return "\n".join(md_lines[::-1])  # 가장 최근에 푼 문제가 가장 상위에 작성되도록


def write_readme(md_lines: str, platform: str):
    """
    플랫폼 별 README 파일 작성
    """
    with open(f"{platform}/README.md", "w", encoding="UTF-8") as readme:
        readme.write(f"## {MD_HEADER[platform]}" + "\n")  # 헤더 작성
        readme.write(md_lines)


def concat_readme(platforms: List[str]):
    """
    전체 README 파일 작성
    """
    with open(f"test.md", "w", encoding="UTF-8") as main_readme:
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
            with open(f"{platform}/README.md", "r", encoding="UTF-8") as readme:
                main_readme.write(readme.read() + "\n")
                main_readme.write("---" + "\n")

if __name__ == "__main__":
    # 윈도우 10 문제 해결
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # 저장된 파일 정보 받아오기
    file_infos_platform = get_FileInfos_by_platform(PLATFORMS)
    print("File 정보 받아옴")
    problems = asyncio.run(get_problems({platform : [file_info.title for file_info in file_infos] for platform, file_infos in file_infos_platform.items()}))
    print("크롤링 완료")
    save_problems(problems)
    print("파일 저장 완료")
    #modify_title(file_infos_platform, problems)
    #print("문제 이름 수정 완료")
    ## 각 플랫폼 별 풀이 내역 작성하기
    #for platform, file_infos in file_infos_platform.items():
    #    md_lines = get_lines(file_infos)
    #    write_readme(md_lines, platform)
    #    print(f"{platform} README 작성 완료")
    ### 전체 풀이 내역 작성하기
    #concat_readme(PLATFORMS)
    #print("전체 README 작성 완료")