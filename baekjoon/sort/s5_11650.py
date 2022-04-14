n = int(input())
pos_list = [list(map(int, input().split())) for _ in range(n)]
pos_list.sort(key = lambda x : (x[0], x[1]))
for x, y in pos_list:
    print(x, y)