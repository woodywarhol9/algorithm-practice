# BFS를 활용한 풀이
from collections import deque
 
def bfs(map_info: list, start: int, end: int, n: int) -> int:
    queue = deque()
    queue.append(start)
    # BFS 시작
    while queue:
        x = queue.popleft()
        # 방문한 경우 종료
        if x == end:
            break
        for i in range(3):
            if i == 0:
                x_new = x * 3
            elif i == 1:
                x_new = x * 2
            else:
                x_new = x + n
            # 방문 가능한 경우에만
            if x_new <= end:
                # 아직 방문하지 않은 경우에만
                if map_info[x_new] == 1:
                    map_info[x_new] = map_info[x] + 1
                    queue.append(x_new)
    # 연산 횟수기 때문에 - 1
    return map_info[end] - 1
    
 
def solution(x, y, n):
    # x와 y가 같은 경우 : 탐색 필요 X
    if x == y:
        return 0
    # y 까지의 정보 저장
    map_info = [1 for i in range(y + 1)]
    cnt = bfs(map_info, x, y, n)
    return cnt if cnt > 0 else -1

# DP를 활용한 풀이
def solution(x, y, n):
    answer = 0
    # DP 테이블 : 최소 횟수 저장
    DP = [0 for _ in range(y + 1)]
    for i in range(x + 1, y + 1):
        # 초기값
        a, b, c = 1e9, 1e9, 1e9
        # 1. X3 확인
        # 3의 배수가 아닌 경우 + x 범위 이전에 온 경우 불가
        if i % 3 == 0 and i / 3 >= x:
            a = DP[i//3]
        # 2. X2 확인
        # 2의 배수가 아닌 경우 + x 범위 이전에 온 경우 불가
        if i % 2 == 0 and i / 2 >= x:
            b = DP[i//2]
        # 3. +N 확인
        # x 범위 이전에 온 경우 불가
        if i - n >= x:
            c = DP[i - n]
        # a, b, c 값이 모두 업데이트 되지 않음 : 접근 불가능
        if a == b == c == 1e9:
            DP[i] = 1e9
        # a, b, c 값 중 최소 값을 결정할 수 있는 경우
        else:
            DP[i] = min(a, b, c) + 1
    return DP[y] if DP[y] != 1e9 else -1