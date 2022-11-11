# 1 : 순열 구현
"""
def get_perm(arr, n):
    perm_list = []
    # 종료 조건
    if n == 0:
        return [[]]
    # 현재 arr의 담긴 수를 확인
    for i in range(len(arr)):
        # 선택된 수
        num = arr[i]
        # 나머지 수로 구성된 배열
        arr_left = arr[:i] + arr[i+1:]
        for perm in get_perm(arr_left, n - 1):
            perm_list.append([num] + perm)
    return perm_list
# 수의 개수
N = int(input())
# 입력 수
num_list = list(map(int, input().split()))
op_cnt = list(map(int, input().split()))
op_list = ["+", "-", "*", "/"]
# 연산자 인덱스 저장
op_idx = []
for i in range(4):
    # 개수 만큼 반복
    for j in range(op_cnt[i]):
        op_idx.append(op_list[i])
# 결과 저장
max_val = -1e9
min_val = 1e9

for perm in get_perm(op_idx, len(op_idx)):
    total = num_list[0]
    for i, op in enumerate(perm):
        if op == "+":
            total += num_list[i + 1]
        elif op == "-":
            total -= num_list[i + 1]
        elif op == "*":
            total *= num_list[i + 1]
        else:
            # 음수 경우 처리
            if total < 0:
                total = - (abs(total) // num_list[i + 1])
            else:
                total //= num_list[i + 1]                        
    if total > max_val:
        max_val = total
    if total < min_val:
        min_val = total
    
print(max_val, min_val, sep = "\n")
"""
# 2 : DFS + 백트래킹
N = int(input())
num_list = list(map(int, input().split()))
op_cnt = list(map(int, input().split()))

# 최댓값, 최솟값 초기화
min_val = 1e9
max_val = -1e9

def dfs(i, now):
    # 값 변경위해서 global 선언
    global min_val, max_val
    if i == N:
        min_val = min(min_val, now)
        max_val = max(max_val, now)
    else:
        # 각 연산자에 대해서 재귀적으로 수행
        # + 연산자
        if op_cnt[0] > 0:
            op_cnt[0] -= 1
            dfs(i + 1, now + num_list[i])
            # 다시 되돌리기
            op_cnt[0] += 1
        # - 연산자
        if op_cnt[1] > 0:
            op_cnt[1] -= 1
            dfs(i + 1, now - num_list[i])
            op_cnt[1] += 1
        # * 연산자
        if op_cnt[2] > 0:
            op_cnt[2] -= 1
            dfs(i + 1, now * num_list[i])
            op_cnt[2] += 1
        # / 연산자
        if op_cnt[3] > 0:
            op_cnt[3] -= 1
            dfs(i + 1, int(now / num_list[i]))
            op_cnt[3] += 1

dfs(1, num_list[0])
# 최댓값 - 최솟값 차례대로 출력
print(max_val, min_val, sep = "\n")
            