import sys
from string import ascii_uppercase
from collections import deque

msg = input()
key = input()
# 중복 제거 및 남은 알파벳 확인
key = deque(set(key))
alpha_left = deque(set(ascii_uppercase) - set(key) - set("J"))
# 암호 표 생성
graph = [[0] * 5 for _ in range(5)]
# idx 정보 hash로 보관
idx_info = {}
for row in range(5):
    for col in range(5):
        if key:
            pop = key.popleft()
            graph[row][col] = pop
            # idx 정보 보관
            idx_info[pop] = [row, col]
        else:
            if alpha_left:
                pop = alpha_left.popleft()
                graph[row][col] = pop
                # idx 정보 보관
                idx_info[pop] = [row, col]
        
msg_list = []
msg = list(msg)

for idx, char in enumerate(msg):
    # 처음은 넘기기
    if idx == 0:
        continue
    # 문자열 넣기
    if idx % 2 == 1:
        # 이전 문자열과 다를 경우 바로 넣어주기
        if msg[idx - 1] != char:
            msg_list.append(msg[idx - 1] + char)
        #같을 경우 중복 처리
        else:
            if char == 'X':
                msg_list.append(msg[idx - 1] + "Q")
                # 다시 처리하도록 넣어주기
                msg.insert(idx + 1, char)
            else:
                msg_list.append(msg[idx - 1] + "X")
                # 다시 처리하도록 넣어주기
                msg.insert(idx + 1, char)
# idx가 짝수로 끝났을 경우 마지막 한 글자가 남으므로 넣어주기.
if idx % 2 == 0:
    msg_list.append(msg[idx] + "X")
# 암호화 진행
for a, b in msg_list:
    a_row, a_col = idx_info[a]
    b_row, b_col = idx_info[b]
    # 같은 행에 존재하면.
    if a_row == b_row:
        a_col = a_col + 1
        b_col = b_col + 1
        if a_col == 5:
            a_col = 0
        if b_col == 5:
            b_col = 0
    # 같은 열에 존재하면
    elif a_col == b_col:
        a_row = a_row + 1
        b_row = b_row + 1
        if a_row == 5:
            a_row = 0
        if b_row == 5:
            b_row = 0
    else:
        a_col, b_col = b_col, a_col

    print(graph[a_row][a_col], end = "")
    print(graph[b_row][b_col], end = "")