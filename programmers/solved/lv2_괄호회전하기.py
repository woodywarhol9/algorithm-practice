# 괄호 회전 -> deque.rotate로 구현
# 올바른 괄호 여부 확인 : stack으로!
from collections import deque

def solution(s):
    # 올바른 괄호 문자열의 수
    answer = 0
    # 올바른 괄호 쌍
    match = {"[" : "]", "(" : ")", "{" : "}"}
    # i 만큼 회전
    for i in range(len(s)):
        s_rot = deque(s)
        # 왼쪽으로 회전
        s_rot.rotate(-i)
        # 올바른 괄호 판별하기
        stack = []
        for c in s_rot:
            if c in ("[", "(", "{"):
                stack.append(c)
            else:
                # ], ), } 가 먼저 나오거나, 쌍이 맞지 않는 경우
                if not stack or match[stack[-1]] != c:
                    break
                else:
                    stack.pop()
        # break가 안 된 경우 -> 길이만 확인하면 됨
        else:
            # stack이 다 제거 된 경우
            if not stack:
                answer += 1
        
    return answer