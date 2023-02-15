n = int(input())
n_list = []
for _ in range(n):
    n_list.append(int(input()))
n_list.sort()
print(*n_list, sep = "\n")