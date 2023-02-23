n = int(input())
sieve = [True] * n

m = int(n ** 0.5)
# 에라토스테네스의 체
for i in range(2, m + 1):
    if sieve[i -1] == True:
        for j in range(i+i, n + 1, i):
            sieve[j - 1] = False

# 소인수 : 소수 + 약수            
prime_factor = [i for i in range(2, n + 1) if sieve[i - 1] == True \
    and n % i == 0]

for factor in prime_factor:
    while True:
        temp = n / factor
        if int(temp) - temp != 0:
            break
        n /= factor
        print(factor)
    