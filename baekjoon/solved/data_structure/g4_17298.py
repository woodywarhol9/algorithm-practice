import sys

n = int(input())
seq = list(map(int, sys.stdin.readline().rstrip().split()))
# nge_list
output_list = [-1] * n
# idx 저장 stack
stack = []

for i in range(n):
    while stack:
        if seq[i] > seq[stack[-1]]:
            output_list[stack.pop()] = seq[i]
        else:
            break
    stack.append(i)

print(*output_list)