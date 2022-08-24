from itertools import combinations

def get_prime(n):
    
    sieve = [True] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    
    return [i for i in range(2, n + 1) if sieve[i] == True]        
    

def solution(nums):
    # 최대 경우
    prime_list = set(get_prime(1000 + 999 + 998))
    comb_list = list(combinations(nums, 3))
    
    cnt = 0
    for comb in comb_list:
        temp = sum(comb)
        if temp in prime_list:
            cnt += 1
    
    return cnt