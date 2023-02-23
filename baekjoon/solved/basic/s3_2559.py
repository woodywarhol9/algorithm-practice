n, k = map(int, input().split())
degree_list = list(map(int, input().split()))

prefix_sum = [0]
total = 0
for i in range(n):
    total += degree_list[i]
    prefix_sum.append(total)
    
max_sum = -1e9
for j in range(n):
    if j + k == n + 1:
        break
    temp_sum = prefix_sum[j + k] - prefix_sum[j]
    if temp_sum >= max_sum:
        max_sum = temp_sum

print(max_sum)