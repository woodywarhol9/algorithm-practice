"""
큐(Queue) : First In First Out(FIFO) / 선입선출
 - Python에선 deque를 queue 구현 시 사용한다.
"""
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() #5가 삭제(제일 먼저 입력 됐으므로!)
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 순서 뒤집기
print(queue)