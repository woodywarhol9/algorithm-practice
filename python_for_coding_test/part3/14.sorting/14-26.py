"""
카드 정렬하기 : 작은 크기의 두 카드 묶음일 때 최적 해 만족. 리스트를 계속 정렬하는 방법도 있지만 우선 순위 큐를 활용하자.
"""
import heapq

n = int(input())

# 힙에 카드 묶음 넣기
heap = []
for _ in range(n):
    data = int(input())
    heapq.heappush(heap, data)

comp_num = 0

# 힙에 원소가 1개일 때까지 진행
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    # 다시 합쳐서 삽입
    sum = first + second
    comp_num += sum
    heapq.heappush(heap, sum)

print(comp_num)
    

