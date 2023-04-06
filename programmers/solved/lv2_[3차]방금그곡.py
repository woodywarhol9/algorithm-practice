# 끝부분-처음 부분 연결돼 헷갈릴 수 있음 / 중간 멜로디만 겹칠 수 있음
# 재생 시간, 제공 악보를 보면서 비교 필요
# 1 분 1 개씩 -> 시간 충분하면 반복 재생 / 짧으면 재생 시간만큼만 !
# 조건 일치 여러개 -> 1. 재생 시간이 제일 긴 음악 제목 반환 2. 먼저 입력된 음악 제목 반환
 
# 샾 문자 -> 변경 필요
def solution(m, musicinfos):
    # 음악 정보 분리
    musicinfos = [info.split(",") for info in musicinfos]
    # 샵 문자 변경
    remove_sharp = {"C#" : "c", "D#" : "d", "F#" : "f", "G#" : "g", "A#" : "a"}
    for pitch, new_pitch in remove_sharp.items():
        m = m.replace(pitch, new_pitch)
        for idx, info in enumerate(musicinfos):
            info = *info[:3], info[3].replace(pitch, new_pitch)
            musicinfos[idx] = info
    # 시간 정보 계산 + 멜로디 계산
    for idx, info in enumerate(musicinfos):
        t1, t2, title, melody = info
        t1_h, t1_m = t1.split(":")
        t2_h, t2_m = t2.split(":")
        # 시간 정보 계산
        t1 = int(t1_h) * 60 + int(t1_m)
        t2 = int(t2_h) * 60 + int(t2_m)
        t = t2 - t1
        # 재생 시간에 맞게 멜로디 수정
        q, r = divmod(t, len(melody))
        melody = q * melody + melody[:r]
        musicinfos[idx] = [t, t1, t2, title, melody]
    # 조건이 일치하는 음악 찾기
    answer = []
    for info in musicinfos:
        idx = info[4].find(m)
        # 찾은 경우
        if idx != -1:
            answer.append(info)
    # 최대 길이 음악 선택
    if answer:
        answer = sorted(answer, key = lambda x : (-x[0], x[1]))
    return answer[0][3] if answer else "(None)"