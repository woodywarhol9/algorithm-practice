"""
에라토스테네스의 체
- 가장 큰 수의 제곱근까지의 소수만 체크하면 된다!
"""

n = int(input())
number_list = list(map(int, input().split()))

max_num = max(number_list)
# 에라토스테네스의 체 초기화
sieve = [True] * (max_num)
# 1은 소수 X
sieve[0] = False
# 최대 배수 설정
m = int(max_num ** 0.5)

for i in range(2, m + 1):
    # i가 소수인 경우
    if sieve[i - 1] == True:
        # i 이후 i의 배수들을 제거
        for j in range(i+i, max_num + 1, i):
            sieve[j - 1] = False

print(len([i for i in number_list if sieve[i - 1] == True]))

