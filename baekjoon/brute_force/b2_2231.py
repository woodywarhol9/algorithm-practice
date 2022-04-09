decompose_sum = {}

for i in range(1, 10**6 + 1):
    sum = i
    for j in str(i):
        sum += int(j)
    decompose_sum[i] = sum 

sum_num = {}
for k, v in decompose_sum.items():
    if v not in sum_num:
        sum_num[v] = k
        
n = int(input())

try:
    print(sum_num[n])

except:
    print(0)