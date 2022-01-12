"""
정렬된 배열에서 특정 수의 개수 구하기 : 문제에 제시된 시간 복잡도 O(logN)을 만족하기 위해서 이진 탐색 활용. bisect_left/right는 target 값이 없을 경우 target이 새로 들어갈 위치를 return(까먹지 말기.)
"""

from bisect import bisect_left, bisect_right

def count_num(num_list, value):
    left_index = bisect_left(num_list, value)
    right_index = bisect_right(num_list, value)
    
    num_len = right_index - left_index
    return num_len
    
    
    
n, x = map(int, input().split())
num_list = list(map(int, input().split()))

x_count = count_num(num_list, x)

if x_count == 0:
    print(-1)
else :
    print(x_count)

