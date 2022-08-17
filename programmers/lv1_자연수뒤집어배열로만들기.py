def solution(n):
    # int를 list에 넣기 위해서 str로 변환 -> map으로 다시 int로 변환
    n_reverse = list(map(int, str(n)))[::-1]
    return n_reverse