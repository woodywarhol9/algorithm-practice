"""
피보나치 : 메모이제이션 구현
"""

# 메모이제이션위한 리스트 초기화
d = [0] * 100

#탑 - 다운 다이나믹 프로그래밍 방식
def fibo(x):
    #종료 조건
    if x == 1 or x == 2:
        return 1
    #이미 계산한 적 있다면 반환
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]
