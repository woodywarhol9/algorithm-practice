import sys
# binary search
from bisect import bisect_left, bisect_right

n = int(input())
num_array = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

m = int(input())
target_array = list(map(int, sys.stdin.readline().rstrip().split()))

count_array = []
for i in target_array:
    # 시작 idx, 끝 idx 구하기
    start, end = bisect_left(num_array, i), bisect_right(num_array, i)
    count_array.append(end - start)
print(*count_array)