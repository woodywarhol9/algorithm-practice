"""
팩토리얼 구현 : 1. 반복문, 2. 재귀
"""

# 1. 반복문으로 구현하기.
def factorial_iterative(n):
    result = 1
    # 1부터 n까지 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 2. 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:  # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!
    return n * factorial_recursive(n - 1)