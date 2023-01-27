def solution(n):
    # n = 0인 경우도 존재
    div_list = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            div_list.append(i)
            # 약수와 곱해진 다른 수도 약수이다.
            if i != n // i:
                div_list.append(n // i)
                
    return sum(div_list)