import sys

def binary_search(wood_h:list, target_h:int):
    start = 1
    end = max(wood_h)
    while start <= end:
        # 자를 높이
        mid = (start + end) // 2
        # 얻을 수 있는 
        cut_h = sum([(i - mid) for i in wood_h if i > mid])
        # 높이를 더 늘려야 함
        if cut_h >= target_h:
            start = mid + 1
        # 높이를 낮춰야 함
        else:
            end = mid - 1
    # 최대 높이
    print(end)
            
wood_num, target_height = map(int, input().split())
wood_height = list(map(int, sys.stdin.readline().rstrip().split()))
binary_search(wood_height, target_height)