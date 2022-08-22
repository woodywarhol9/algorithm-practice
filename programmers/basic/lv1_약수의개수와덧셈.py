def get_divisor(n):
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt += 1
        if (n % (n // i)) == 0 and (i != n // i):
            cnt += 1
    return cnt
            

def solution(left, right):
    result = 0
    for i in range(left, right + 1):
        temp = get_divisor(i)
        result += i * (-1) ** (temp % 2)
    
    return result