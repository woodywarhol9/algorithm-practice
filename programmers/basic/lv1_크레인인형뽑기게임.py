from collections import deque

def solution(board, moves):
    # 남은 열 개수
    len_list = dict(zip(range(1, len(board) + 1), [0] * len(board)))
    # 남은 열 저장
    for idx, col in enumerate(zip(*board[::-1])):
        col = list(col)
        # 0 처리
        for i in col[:]:
            if i == 0:
                col.remove(i)
        len_list[idx + 1] = deque(col)
    # 초기값 0
    stack = deque([0])
    # 사라진 인형 개수
    cnt = 0
    for m in moves:
        if len_list[m]:
            new = len_list[m].pop()
            if new == stack[-1]:
                stack.pop()
                cnt += 2
            else:
                stack.append(new)
    return cnt