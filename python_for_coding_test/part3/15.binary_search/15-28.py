"""
고정점 찾기 : binary_search 구현할 수 있는 지 확인. 자꾸 쳐보면서 익숙해지자.
"""

def binary_search(num_list, start, end):
    # 못 찾으면 start가 더 커지게 되므로
    if start > end:
        return None
    mid = (start + end) // 2
    # 고정점을 찾은 경우 인덱스 반환
    if num_list[mid] == mid:
        return mid
    # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    elif num_list[mid] > mid:
        return binary_search(num_list, start, mid - 1)
    # 중간점이 가리키는 위치의 값보다 중간점이 큰 경우 오른쪽 확인
    else:
        return binary_search(num_list, mid + 1, end)
            
n = int(input())
num_list = list(map(int, input().split()))

# 이진 탐색(Binary Search) 수행
index = binary_search(num_list, 0, n - 1)

# 고정점이 없는 경우 -1 출력
if index == None:
    print(-1)
else:
    print(index)
