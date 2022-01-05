"""
연산자 끼워 넣기
"""
from collections import deque 

num_max = int(1e9)
num_min = int(-1e9)

# 입력 받기
N = int(input())
num_list = list(map(int, input().split()))
op_list = list(map(int, input().split()))

result = 0
queue = deque(num_list)

# 초기 q 설정
count = 0
while queue:
    # 처음엔 queue에서 2개 꺼냄
    if count == 0:
        num1 = queue.popleft()
        num2 = queue.popleft()
    
    else:
        num1 = result
        num2 = queue.popleft()
    
    for i in range(4):
        if i == 0 and op_list[0] > 0:
            result = num1 + num2
            op_list[0] -= 1
            queue.append(result)
        if i == 1 and op_list[1] > 0:
            result = num1 - num2
            op_list[1] -= 1
            queue.append(result)
        if i == 2 and op_list[2] > 0:
            result = num1 * num2
            op_list[2] -= 1
            queue.append(result)
        if i == 3 and op_list[3] > 0:
            result = num // num2
            op_list[3] -= 1
            queue.append(result)
        
print(max(num_max, result))
print(min(num_min, result))

