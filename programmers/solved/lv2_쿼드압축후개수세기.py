# (0의 개수, 1의 개수)
# 재귀? -> 길이가 2일 때 까지 반복 실행
# 압축된 경우 -> 개수 먼저 세기 / 나머지 -> 마지막에 한 번에
cnt = [0, 0]
 
def get_units(n):
    zeros = [[0 for _ in range(n)] for _ in range(n)]
    ones = [[1 for _ in range(n)] for _ in range(n)]
    return zeros, ones
 
def quad_zip(arr, n):
    global cnt
    # 바로 구성할 수 있는 경우
    zeros, ones = get_units(n)
    if arr == zeros:
        cnt[0] += 1
        return
    elif arr == ones:
        cnt[1] += 1
        return
    # 더 이상 쪼갤 수 없는 경우
    if n == 2:
        for nums in arr:
            for num in nums:
                if num == 0: cnt[0] += 1
                else: cnt[1] += 1
        return
    # 쪼갤 수 있는 경우
    zeros, ones = get_units(n // 2)
    # 압축 가능한 지 확인
    for i in range(0, n, n // 2):
        for j in range(0, n, n // 2):
            quad = [row[j : j + n // 2] for row in arr[i : i + n // 2]]
            if quad == zeros:
                cnt[0] += 1
            elif quad == ones:
                cnt[1] += 1
            else: quad_zip(quad, len(quad))
    return
 
def solution(arr):
    quad_zip(arr, len(arr))
    return cnt