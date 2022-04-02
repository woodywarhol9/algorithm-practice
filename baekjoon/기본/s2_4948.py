while True:
    n = int(input())
    if n == 0:
        break
    sieve = [True] * (2 * n)
    m = int((2 * n) ** 0.5)
    for i in range(2, m + 1):
        if sieve[i - 1] == True:
            for j in range(i + i, 2*n + 1, i):
                sieve[j - 1] = False
    
    prime_number = [i for i in range(2, 2*n +1) if sieve[i - 1] == True \
        and i > n]    
    print(len(prime_number))