# 1 ~ n 까지의 택배를 재 배열
# 기존 컨테이너 : queue -> 작은 수부터 빼낼 수 있음
# 보조 컨테이너 : Stack -> 큰 수부터 빼낼 수 있음
# 몇 개의 상자를 실을 수 있는지
# order의 상자가 나올 때 까지 pop

from collections import deque

def solution(order):
    order = deque(order)
    # 메인 컨베이어 작업 목록
    main_line = deque(range(order[0] ,len(order) + 1))
    # 서브 컨베이어 작업 목록
    sub_line = list(range(1, order[0]))
    # 개수 확인
    cnt = 0
    # 꺼낼 main이 있는지 확인
    flag = True
    while flag and order:
        order_now = order.popleft()
        while True:
            # 메인에 있는 경우
            if main_line and main_line[0] == order_now:
                main_line.popleft()
                cnt += 1
                break
            # 서브에 있는 경우
            if sub_line and sub_line[-1] == order_now:
                sub_line.pop()
                cnt += 1
                break
            # 둘 다에 없는 경우
            if not main_line:
                flag = False
                break
            else:
                sub_line.append(main_line.popleft())
    return cnt


# 보조 컨베이어 벨트(Stack)에 항상 옮기는 방식으로 푼 풀이
"""
def solution(order):
    assist = []
    i = 1
    cnt = 0 
    while i != len(order)+1:
        assist.append(i)
        while assist and assist[-1] == order[cnt]:
            cnt += 1
            assist.pop()
            
        i += 1
    return cnt
"""