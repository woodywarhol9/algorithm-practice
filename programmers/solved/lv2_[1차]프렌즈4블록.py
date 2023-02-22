# (2 x 2) -> 한번에 제거 -> 판별을 어떻게 할 것인지???
# 왼쪽 상위 좌표 [i, j] 기준 완전 탐색
# 제거된 후 블럭이 내려옴 -> 어떻게 처리 -> 열 별로 맵 탐색 -> 0 나오면 swap...
 
def solution(m, n, board):
    board = list(map(list, board))
    cnt = 0
    # 2 x 2 블록의 왼쪽 상위 좌표 탐색
    # 제거할 수 없을 때 까지 반복
    while True:
        # 제거할 박스 정보 저장
        hit_box = set()
        for i in range(m - 1):
            for j in range(n - 1):
                lt, ld, rt, rd = board[i][j], board[i + 1][j], board[i][j + 1], board[i + 1][j + 1]
                # 제거할 블록인지 확인
                # 이미 빈 칸인 경우 개수 세지 않음
                if lt == ld == rt == rd and lt != 0:
                    hit_box.add((i, j))
                    hit_box.add((i + 1, j))
                    hit_box.add((i, j + 1))
                    hit_box.add((i + 1, j + 1))
        # 더 이상 제거될 블록이 없다면 종료
        if not hit_box: break
        # 제거한 블록 개수 더하기
        cnt += len(hit_box)
        # 블록 제거
        for hit in hit_box:
            hit_i, hit_j = hit
            board[hit_i][hit_j] = 0
        # 블록 이동 : 열 단위로 진행
        for j in range(n):
            # 0일 경우 swap
            for i in range(m):
                for ii in range(1, m - i):
                    if board[ii][j] == 0:
                        # 맨 위로 보내기 위해서 [ii -1] 과 [i]를 swap
                        board[ii - 1][j], board[ii][j] = board[ii][j], board[ii - 1][j]
    return cnt