n, m = map(int, input().split())

# 최대 공약수
for i in range(max(n, m), 0, -1):
    if n % i == 0 and m % i == 0:
        print(i)
        break
# 최소 공배수
for i in range(min(n, m), n * m + 1):
    if i % n == 0 and i % m == 0:
        print(i)
        break

