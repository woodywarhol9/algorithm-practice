# 자신보다 뒤 + 크면서 가장 가까이 있는 수 : 뒷 큰수
# 뒷 큰수가 없으면 -1
# 완전 탐색 불가

# 큰 수가 없으면, 큰 수가 나올 때 까지 보관하고 확인해야 함
# 그러다가 큰 수가 나오면 바로 제거
# 스택을 활용해서 풀 수 있음

def solution(numbers):
    # 정답 정보
    answer = [-1] * len(numbers)
    # 스택
    stack = []
    for idx, num in enumerate(numbers):
        # 큰 수가 나온 경우, 그 수를 사용해 정답 정보 갱신
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(idx)
    
    return answer