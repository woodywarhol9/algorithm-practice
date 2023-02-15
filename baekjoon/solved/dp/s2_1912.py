import sys

n = int(input())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

max_sum = -1e9
temp = 0
for i in num_list:
    temp += i
    if max_sum < temp:
        max_sum = temp
    # 합이 0보다 작다면 새로 합을 구함
    if temp < 0:
        temp = 0
print(max_sum)    