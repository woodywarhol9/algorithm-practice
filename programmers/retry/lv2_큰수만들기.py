# 가장 큰 수 : 맨 앞자리가 가장 커야 함
# 한번 제거된 수는 다시 사용되지 않기 때문에 Stack으로 처리할 수 있음
def solution(number, k):
    stack = []
    for n in number:
        # 새로 입력될 숫자가 기존보다 클 경우
        # 변경 진행
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)
    # 아직 제거하지 못한 숫자를 뒤에서부터 삭제
    # 제거되지 못한 경우 : 동일한 숫자가 반복된 경우 / K개를 지웠지만 아직 남은 숫자가 있는 경우
    if k > 0:
        stack = stack[:-k]
    return "".join(stack)