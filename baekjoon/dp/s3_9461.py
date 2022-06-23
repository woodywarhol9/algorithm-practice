T = int(input())
p_list = [1, 1, 1, 2, 2]

for i in range(4, 100):
    p_list.append(p_list[i] + p_list[i - 4])

for _ in range(T):
    n = int(input())
    print(p_list[n - 1])