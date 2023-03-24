# 재귀를 활용한 풀이
arr = []
 
 
def draw(x, y, cnt, num):
    if cnt < 1:
        return
    number = num
    # 삼각형의 좌측 대각선
    for i in range(cnt):
        arr[x + i][y] = number
        number += 1
    # 삼각형의 밑변
    for i in range(1, cnt):
        arr[x + cnt - 1][y + i] = number
        number += 1
    # 삼각형의 우측 대각선
    for i in range(1, cnt - 1):
        arr[x + cnt - 1 - i][y + cnt - 1 - i] = number
        number += 1
    # 삼각형의 새로운 시작 점
    # 시작점 x : 1 -> 3 -> 5 -> ...
    # 시작점 y : 1 -> 2 -> 3 -> ...
    draw(x + 2, y + 1, cnt - 3, number)
 
 
def solution(n):
    global arr
    arr = [[0] * n for _ in range(n)]
    draw(0, 0, n, 1)
 
    answer = []
    for i in range(n):
        for j in range(i + 1):
            answer.append(arr[i][j])
    return answer
# N개의 직선으로 분리해서 접근하는 풀이
"""
# 3 번의 실행 마다, 채워지는 위치가 달라짐 | 왼쪽 대각선 -> 밑변 -> 오른쪽 대각선
# 매번 채우는 개수가 달라짐 | n -> n - 1 -> n - 2 ...
 
def solution(n):
    tri_info = [[0 for _ in range(n)] for _ in range(n)]
    # 채워 넣을 숫자
    num = 1
    # 채워 넣을 위치
    x, y = -1, 0
    # 한 줄 단위로 채우기
    for i in range(n):
        # 채울 수의 개수
        for _ in range(i, n):
            # 왼쪽 대각선을 채울 경우
            if i % 3 == 0:
                x += 1
            # 밑변을 채울 경우
            elif i % 3 == 1:
                y += 1
            # 오른쪽 대각선을 채울 경우
            else:
                x -= 1
                y -= 1
            # 채우기
            tri_info[x][y] = num
            num += 1
    # 1개의 행으로 변경하기
    answer = []
    for row in tri_info:
        answer.extend(sum([], [e for e in row if e != 0]))
    return answer
"""