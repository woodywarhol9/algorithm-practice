# 소수 판별
# 1111111111111111111111 과 같은 경우 생각하면, 에라토스테네스의 체 활용 불가!
def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True
# n 진법 변환
def get_nbase(n, k):
    r_list = ""
    while n:
        q, r = divmod(n, k)
        # 나머지를 모아 n 진법 표현
        r_list += str(r)
        n = q
    return r_list[::-1]
 
import re
 
def solution(n, k):
    # 조건에 맞는 소수의 개수
    prime_cnt = 0
    # n 진법으로 변환
    nbase = get_nbase(n, k)
    # 정규 표현식 패턴
    re_pt = r"(0[1-9]+0)|(^[1-9]+0)|(0[1-9]+$)|([1-9]+)"
    pt = re.findall(re_pt, nbase)
    for p in pt:
        # 그룹 묶기
        p = "".join(p)
        # 0 제거
        p = p.replace("0", "")
        if is_prime(int(p)):
            prime_cnt += 1
    
    return prime_cnt