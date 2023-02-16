# K가 10억 -> 반복 횟수가 매우 큼
# 100 만의 길이를 계속 정렬한다면 시간 초과가 발생할 듯
from heapq import heappush, heappop, heapify

def solution(scoville, K):
    # 실행 횟수
    cnt = 0
    # 최소힙으로 변경
    heapify(scoville)
    while True:
        # 가장 맵지 않은
        s1 = heappop(scoville)
        # 가장 안 매운 음식이 K 넘으면, 나머지는 확인할 필요 X
        if s1 >= K:
            break
        # 두 번째로 맵지 않은
        if scoville:
            s2 = heappop(scoville)
        # 구성 못한 경우
        else:
            cnt = -1
            break
        # 섞기
        s = s1 + (s2 * 2)
        heappush(scoville, s)
        cnt += 1
    
    return cnt