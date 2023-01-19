import heapq

def solution(k, score):
    answer = []
    # 최하 점수만 확인하면 되기 때문에 heapq 사용
    heap = []
    for i in score:
        heapq.heappush(heap, i)
        # 개수 초과 시 제거
        if len(heap) > k:
            heapq.heappop(heap)
        answer.append(heap[0])
    return answer