import sys

def binary_search(target):
    # index를 찾자
    start = 0
    end = j_class - 1
    while start <= end:
        mid = (start + end) // 2
        count = sum(w_list[:mid + 1]) # idx 찾기 위해서 mid + 1
        if count <= target:
            start = mid + 1
        elif count > target:
            end = mid - 1
    return mid

bag, j_class = map(int, input().split())
# 무게당 가격으로 정렬
# counting sort 사용
counting = [0] * (10**4 + 1)
for _ in range(j_class):
    w, p = map(int, input().split())
    if counting[p] == 0:
        counting[p] = [w, p]
    # 동일 무게 존재
    else:
        counting[p][0] = counting[p][0] + w
j_info = []
for i in range(10 ** 4, 0, -1):
    if counting[i] == 0:
        continue
    j_info.append(counting[i])
w_list, val_list = zip(*j_info)
# binary search로 idx 얻기
idx = binary_search(bag)
# 무게 계산
weight = sum(w_list[:idx])
val = sum([w_list[i] * val_list[i] for i in range(idx)])
# 가방 무게 확인
bag -= weight
val += bag * val_list[idx]
print(val)