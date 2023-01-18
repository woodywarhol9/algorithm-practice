def solution(s):
    char_set = {}
    # -1로 초기화
    answer = [-1] * len(s)
    for i, char in enumerate(s):
        # 문자가 이미 나온 경우
        if char in char_set:
            answer[i] = i - char_set[char]
        # 위치 정보 업데이트
        char_set[char] = i 
            
    return answer