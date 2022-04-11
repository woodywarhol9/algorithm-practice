m, n = map(int, input().split())
board = []
for _ in range(m):
    board.append(input())

color = {0 : "B", 1 : "W"}

paint_list = []
# 시작점 찾기
for x_start in range(m - 7):
    for y_start in range(n - 7):
        # 색칠 개수
        paint = 0
        # 흰색, 검은색 시작 경우
        paint_w, paint_b = 0, 0
        for x in range(x_start, x_start + 8):
            for y in range(y_start, y_start + 8):
                    # 검은색 시작일 때 틀린 경우
                    if board[x][y] != color[(x + y)%2]:
                        paint_b += 1            
                    # 흰색 시작일 때 틀린 경우                
                    else:
                        paint_w += 1
        paint = min(paint_b, paint_w)                
        paint_list.append(paint)

print(min(paint_list))
                
                            
                        
                        
    
                        
                    
        
        