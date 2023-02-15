n = int(input())

num_list = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            num_list[i][0] += num_list[i - 1][0]
        elif j == i:
            num_list[i][-1] += num_list[i - 1][-1]
        else:
            num_list[i][j] += max(num_list[i - 1][j], num_list[i - 1][j - 1])

print(max(num_list[-1]))