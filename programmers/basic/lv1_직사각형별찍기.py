a, b = map(int, input().strip().split(' '))

result = ["*" * a for _ in range(b)]
print(*result, sep = "\n")