from string import ascii_lowercase

def solution(s):
    # 중복 문자 aa, bb 패턴
    pattern = [i * 2 for i in list(ascii_lowercase)]
    stack = []
    for char in s:
        stack.append(char)
        if str("".join(stack[-2:])) in pattern:
            for j in range(2):
                stack.pop()    
    if not stack:
        return 1
    else:
        return 0
"""
def solution(s):
    answer = 0
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
            continue
        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        answer = 1
    return answer
"""