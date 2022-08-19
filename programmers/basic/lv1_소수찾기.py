def get_prime(n):
    
    sieve = [True] * (n + 1)
    m = int(n ** 0.5)
    
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    
    return [i for i in range(2, n + 1) if sieve[i] == True]

def solution(n):
    prime_list = get_prime(n)
    return len(prime_list)