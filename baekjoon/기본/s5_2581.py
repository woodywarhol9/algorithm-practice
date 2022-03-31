start = int(input())
end = int(input())

# 에라토스테네스의 체
sieve = [True] * end
m = int(end ** 0.5)

for i in range(2, m + 1):
    if sieve[i - 1] == True:
        for j in range(i + i, end + 1, i):
            sieve[j - 1] = False

prime_number = [i for i in range(2, end + 1) if sieve[i - 1] == True\
    and i >= start]

if len(prime_number) == 0:
    print(-1)

else:
    print(sum(prime_number))
    print(min(prime_number))
    