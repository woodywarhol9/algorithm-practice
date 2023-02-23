"""
매 실행 마다 이전 패턴을 8번 반복해야 함.
"""
def draw_star(n):
    global paper
    # draw_star(3)
    if n == 3:
        for i in range(3):
            for j in range(3):
                if i == j == 1:
                    continue
                paper[i][j] = 1
        # draw_star(3) 종료
        return   
    
    a = n // 3
    draw_star(a)
    # 기존 패턴 반복
    for i in range(3):
        for j in range(3):
            # 가운데만 비워 놓기
            if i == j == 1:
                continue
            # 행 단위로 복사
            for k in range(a):
                paper[a*i + k][a*j : a*(j + 1)] = paper[k][:a] 
    
n = int(input())

paper = [[0 for _ in range(n)] for _ in range(n)]
draw_star(n)
# 각 행 접근
for i in paper:
    # 각 열 접근
    for j in i:
        if j == 1 :
            print("*", end = "")
        else:
            print(" ", end = "")
    print()