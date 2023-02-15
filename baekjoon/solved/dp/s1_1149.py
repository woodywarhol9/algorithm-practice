n = int(input())

num_list = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    num_list[i][0] += min(num_list[i - 1][1], num_list[i - 1][2])
    num_list[i][1] += min(num_list[i - 1][0], num_list[i - 1][2])
    num_list[i][2] += min(num_list[i - 1][0], num_list[i - 1][1])

print(min(num_list[-1]))