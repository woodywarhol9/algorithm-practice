def solution(absolutes, signs):
    result = [absolutes[i] * (-1) ** (int(signs[i]) + 1) for i in range(len(signs))]
    return sum(result)