import sys

def binary_search(cable_len : list, target_count : int):
    # 케이블 최대 길이 구하기
    start = 1
    end = max(cable_len)
    # result를 따로 추가해 헷갈리지 않게.
    result = 0
    while start <= end:
        mid = (start + end) // 2
        cable_count = [(i // mid) for i in cable_len]
        # 길이를 더 짧게
        if sum(cable_count) < target_count:
            end = mid -1
        # 길이를 더 길게
        elif sum(cable_count) >= target_count:
            # result에 최종 값 저장
            result = mid
            start = mid + 1
    print(result)
            
            
        

cable_num, target_count = map(int, input().split())
cable_len = [int(sys.stdin.readline().rstrip()) for _ in range(cable_num)]
binary_search(cable_len, target_count)
