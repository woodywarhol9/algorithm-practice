"""
피보나치 : 재귀 함수 구현
"""
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)