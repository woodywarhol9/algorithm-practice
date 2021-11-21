"""
퀵 정렬 : 피벗을 기준으로 양쪽을 나누자.   
"""
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: #원소가 1개인 경우 종료
        return
    pivot = start #pivot 설정
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: #엇갈린다면 작은 데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else : #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    #분할 이후 각각 정렬 수행
    quick_sort(array, start, right -1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) -1)
print(array)