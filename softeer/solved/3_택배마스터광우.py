import sys
from itertools import permutations

n, m, k = map(int, input().split())
rail_info = list(map(int, input().split()))
# N이 작기 때문에 모든 경우의 수 확인
cases = list(permutations(rail_info, n))

min_sum = 1e9
# 완전 탐색
for case in cases:
    # 각 탐색마다 k 횟수만큼 시행
    case_sum = 0
    idx = 0
    for i in range(k):
        temp_sum = 0
        while True:
            temp_sum += case[idx % n]
            # 바구니 무게 초과
            if temp_sum > m:
                temp_sum -= case[idx % n]
                # 최소 무게 저장
                case_sum += temp_sum
                break
            else:
                idx += 1
    min_sum = min(min_sum, case_sum)

print(min_sum)