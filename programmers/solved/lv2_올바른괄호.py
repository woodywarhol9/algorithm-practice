def solution(s):
    # 짝 확인
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            # 짝 불가능
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0