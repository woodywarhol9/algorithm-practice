from collections import deque

def solution(progresses, speeds):
    # 배포 / 개발 속도
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    answer = []
    deploy_list = []
    
    while progresses:
        # 하루 작업 진행
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            # 배포 가능
            if progresses[0] >= 100 and progresses[i] >= 100:
                deploy_list.append(i)
        # 배포 프로그램 선정
        if deploy_list:
            now = 0
            cnt = 1
            # 차례대로 배포 : 이전 idx와 1 차이
            for j in deploy_list[1:]:
                if j - now == 1:
                    now = j
                    cnt += 1
                    continue
                else:
                    break
            # 배포 가능 개수
            answer.append(cnt)
            # 배포 후 제거
            for _ in range(cnt):
                progresses.popleft()
                speeds.popleft()  
        # 초기화
        deploy_list = []
        
    return answer