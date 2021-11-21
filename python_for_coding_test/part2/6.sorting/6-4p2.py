"""
파이써닉 퀵 정렬   
"""

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    
    #종료 조건
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:] #피벗을 제외한 리스트
    
    #pivot 기준 분할
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))