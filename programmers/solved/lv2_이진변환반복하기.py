def solution(s):
    # 이진 변환 횟수, 0 개수
    answer = [0, 0]
    while s != "1":
        zero_cnt = len(s)
        s = s.replace("0", "")
        answer[0] += 1
        # 제거된 0의 개수
        answer[1] += (zero_cnt - len(s))
        s = bin(len(s))[2:]
    return answer