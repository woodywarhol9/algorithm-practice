from collections import deque

def solution(priorities, location):
    # 위치 / 우선 순위 저장
    queue = deque(range(len(priorities)))
    priorities = deque(priorities)
    
    answer = 0
    while True:
        # 우선 순위 최고 값인 경우
        max_temp = max(priorities)
        if max_temp == priorities[0]:
            priorities.popleft()
            loc_temp = queue.popleft()
            answer += 1
            # 정답
            if loc_temp == location:
                break
        # 만족 X면 회전
        else:
            priorities.rotate(-1)
            queue.rotate(-1)
            
    return answer