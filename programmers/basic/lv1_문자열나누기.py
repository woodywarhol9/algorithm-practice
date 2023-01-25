def solution(s):
    answer = 0
    word = ""
    # 개수 세기
    x_cnt, y_cnt = 0, 0
    for char in s:
        # 새로운 단어 생성
        if not word:
            word += char
            x_cnt += 1
            continue
        # 글자 확인
        if char == word[0]:
            x_cnt += 1
        elif char != word[0]:
            y_cnt += 1
        # 문자열 분리
        if x_cnt == y_cnt:
            answer += 1
            word = ""
    # 분리되지 못한 경우
    if word:
        answer += 1
    return answer       