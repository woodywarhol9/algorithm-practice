import sys

n = int(input())
num_list = []

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        num_list.pop()
        continue
    num_list.append(num)

print(sum(num_list))