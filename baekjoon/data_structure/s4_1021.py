from collections import deque
import copy

queue_size, num = map(int, input().split())
pos_list = list(map(int, input().split()))
# 회전 큐 (앞, 뒤 경우 생성)
queue = deque([i for i in range(1, queue_size + 1)])

count = 0
for pos in pos_list:
    # 
    if queue[0] == pos:
        queue.popleft()
        continue
    else:
        temp_front = copy.deepcopy(queue)
        temp_back = copy.deepcopy(queue)
        for _ in range(queue_size // 2):
            temp_front.rotate(-1)
            temp_back.rotate(1)
            count += 1
            if temp_front[0] == pos:
                temp_front.popleft()
                queue = copy.deepcopy(temp_front)     
                break
            elif temp_back[0] == pos:
                temp_back.popleft()
                queue = copy.deepcopy(temp_back)
                break
print(count)