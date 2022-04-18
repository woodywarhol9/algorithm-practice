"""
pop(0)가 많이 사용되므로 deque 불러와서 풀이.
"""
from collections import deque

n = int(input())
queue = deque([i for i in range(1, n + 1)])
for _ in range(n - 1):
    queue.popleft()
    queue.append((queue.popleft()))
print(queue[0])