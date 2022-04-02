start, end = map(int, input().split())

sieve = [True] * end
m = int(end ** 0.5)


for i in range(2, m + 1):
    if sieve[i-1] == True:
        for j in range(i+i, end + 1, i):
            sieve[j-1] = False
            
prime_number = [i for i in range(2, end + 1) if sieve[i-1] == True \
    and  i >= start]

print(*prime_number, sep = "\n")