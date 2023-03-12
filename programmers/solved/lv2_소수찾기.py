# 가능한 문자열 구성하기
def dfs(numbers, n_len, num):
    global cnt, is_used, num_uniq
    # 문자열 길이 최대일 경우
    if n_len == len(numbers):
        return
    for i in range(len(numbers)):
        if not is_used[i]:    
            num += numbers[i]
            is_used[i] = 1
            # 숫자 추가
            num_uniq.add(int(num))
            # 새로운 숫자 조합 찾기
            dfs(numbers, n_len + 1, num)
            num = num[:-1]
            is_used[i] = 0
        
def is_prime(n):
    # 소수 판별
    if n <= 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True
    
def solution(numbers):
    # 종이 조각으로 만들 수 있는 숫자
    global num_uniq
    num_uniq = set()
    # 종이(숫자) 사용 여부 확인
    global is_used
    is_used = [0] * len(numbers)
    dfs(numbers, 0, "")
    # 소수인 수 개수 확인
    return len([i for i in num_uniq if is_prime(i)])