"""
N가 50만
- sys.stdin.readline().restrip()으로 입력 받음.
- O(NlogN) 시간 복잡도로 해결 가능하기 때문에 파이썬 기본 정렬 활용.
"""

import sys

n = int(input())
num_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
num_list.sort()
# 숫자 별 횟수 세기
num_count = {}
for num in num_list:
    if num not in num_count:
        num_count[num] = 0
    num_count[num] += 1
# 최대 반복 횟수    
max_count = max(num_count.values())
max_count_nums = sorted([k for k, v in num_count.items() if v == max_count])
max_count_num = max_count_nums[0] if len(max_count_nums) == 1 \
    else max_count_nums[1]

print(round((sum(num_list) / n)))
print(num_list[n // 2])
print(max_count_num)
print(max(num_list) - min(num_list))
