import sys

def binary_search(array,target):
    start = 0
    end = len(array) - 1
    # 원소가 1개인 경우도 있으니 '='으로.
    while start <= end:
        # mid값 계속 변경
        mid = (start + end) // 2
        if array[mid] == target:
            print(1)
            break
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    else:
        print(0)


n = int(input())
# 이진 탐색 위해 정렬
num_array = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
m = int(input())
target_array = list(map(int, sys.stdin.readline().rstrip().split()))

for i in target_array:
    binary_search(num_array, i)