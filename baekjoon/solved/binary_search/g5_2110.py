import sys
# 공유기 설치 개수를 만족하면서 최대 거리를 찾는 것이 목적
def binary_search(house_pos : list, target_num : int):
    # 최소 거리
    start = 1
    # 최대 거리
    end = house_pos[-1] - house_pos[0]
    # 결과 저장
    result = 0
    while start <= end:
        mid = (start + end) // 2
        # 초기 위치는 고정
        router_pos = house_pos[0]
        # 공유기 개수 초기화
        count = 1
        for i in range(1, len(house_pos)):
            if house_pos[i] >= router_pos + mid:
                count += 1
                # 위치 초기화
                router_pos = house_pos[i]
        # 거리를 최대화해야 하기 때문에 count가 target_num 보다 적은 경우부터 고려됨.  
        if count < target_num:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    print(result)
    
house_num, router_num = map(int, input().split())
house_pos = sorted([int(sys.stdin.readline().rstrip()) for _ in range(house_num)])
binary_search(house_pos, router_num)