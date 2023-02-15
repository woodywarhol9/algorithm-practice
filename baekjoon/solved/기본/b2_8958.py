T = int(input())

for _ in range(T):
    problem = input()
    count = 0
    sum = 0
    for p in problem:
        if p == "O":
            count += 1
        else:
            count = 0
        sum += count
    print(sum)
        