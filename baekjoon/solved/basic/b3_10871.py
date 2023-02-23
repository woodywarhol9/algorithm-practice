"""
불필요한 반복 줄이기
"""
N, X = map(int, input().split())
num_list = list(map(int, input().split()))

for num in num_list:
    if X > num:
        print(num, end = " ")