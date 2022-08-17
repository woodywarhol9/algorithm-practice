def solution(num):
    # num = 1인 경우
    result = -1
    if num == 1:
        result = 0
        return result
    # num != 1인 경우
    cnt = 0
    while cnt <= 500:
        if num == 1:
            break
        else:
            cnt += 1
            if num % 2 == 0:
                num /= 2
            else:
                num *= 3
                num += 1
    if cnt > 500:
        result = -1
    else:
        result = cnt
    return result