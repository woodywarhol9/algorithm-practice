from collections import deque

def dfs(numbers, target):
    cnt = 0
    
    queue = deque()
    # +, - 시작
    queue.append([numbers[0], 0])
    queue.append([-numbers[0], 0])
    while queue:
        # stack 처리
        val, idx = queue.pop()
        idx += 1
        if idx < len(numbers):
            queue.append([val +numbers[idx], idx])
            queue.append([val -numbers[idx], idx])
        else:
            if val == target:
                cnt += 1    
    return cnt
            
def solution(numbers, target):
    answer = dfs(numbers, target)
    return answer