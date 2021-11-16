'''
아이디어 : 방문 여부를 표시할 맵을 따로 생성하자.
'''

def turn_counter_clockwise():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

#맵 크기 입력
n, m = map(int, input().split())

#방문 여부
x, y, direction = map(int, input().split())
is_visit = [[0] * m for i in range(n)]
is_visit[x][y] = 1

#map의 외곽은 항상 1으로 설정
map_info = []
for i in range(n):
    map_info.append(list(map(int, input().split()))) #map 함수의 반환 값은 map 객체이기 때문에 다른 자료형으로 변환

#북, 동, 남, 서 (0,1,2,3)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


count = 1
init_direc = direction

#탐험 시작
while True:
    turn_counter_clockwise()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if is_visit[nx][ny] == 0 and map_info[nx][ny] == 0:
        is_visit[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        init_direc = direction
        continue #다시 실행
    
    #네 방향 모두 갈 수 없을 때 : 한 바퀴 돌아서 원래 방향으로 돌아왔을 경우
    if init_direc == direction:
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤로 이동
        if map_info[nx][ny] == 0:
            x = nx
            y = ny
        
        else:
            break

print(count)
        

