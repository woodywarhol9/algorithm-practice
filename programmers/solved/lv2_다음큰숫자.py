# 다음 큰 숫자 : 'n보다 크고, 2 진수 표현에서 1의 갯수가 같은 수' 중에서 가장 작은 숫자
# 시간 복잡도 : n * ((logc + c) * c)
def solution(n):
    n_cnt = bin(n)[2:].count("1")
    check = n + 1
    while True:
        if bin(check)[2:].count("1") == n_cnt:
            return check
        check += 1