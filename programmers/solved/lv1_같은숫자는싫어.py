from collections import deque

def solution(arr):
    
    answer = deque([-1])
    while arr:
        pop = arr.pop()
        if pop != answer[-1]:
            answer.append(pop)
    # -1 제거
    answer.popleft()
    answer.reverse()
    answer = list(answer)
    return answer