n = int(input())

size = []
for _ in range(n):
    size.append(tuple(map(int, input().split())))

rank = 1
for weight, height in size:
    for a, b in size:
        if a == weight and b == height:
            continue
        if a > weight and b > height:
            rank += 1
    print(rank, end = " ")
    rank = 1