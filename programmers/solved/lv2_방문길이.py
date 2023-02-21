# 이동 처리
def move(d, x, y):
    if d == "U":
        if x - 1 >= 0: x -= 1
    elif d == "D":
        if x + 1 <= 10: x += 1
    elif d == "R":
        if y + 1 <= 10: y += 1
    elif d == "L":
        if y - 1 >= 0: y -= 1
    return x, y
 
# 이동 체크 필요
def solution(dirs):
    # 방문 여부 확인
    is_visited = set()
    # 시작 위치
    x, y = 5, 5
    for d in dirs:
        # 이동
        nx, ny = move(d, x, y)
        # 이동 안한 경우 처리
        if nx == x and ny == y:
            continue
        # 방문 처리(돌아올 경우 포함)
        is_visited.add(f"{x}{nx}-{y}{ny}")
        is_visited.add(f"{nx}{x}-{ny}{y}")
        # 좌표 변경
        x, y = nx, ny
    return len(is_visited) // 2