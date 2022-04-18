"""
circular_queue를 통해 풀이.
"""
from collections import deque

n, k = map(int, input().split())
circular_queue = deque([i for i in range(1, n + 1)])
num_list = []
for _ in range(n):
    circular_queue.rotate(-k + 1)
    num_list.append(circular_queue.popleft())

print("<", end="")
print(*num_list, sep = ", ", end="")
print(">")