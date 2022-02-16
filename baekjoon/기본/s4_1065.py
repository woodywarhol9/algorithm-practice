"""
1. 정렬된 리스트니까 bisect 활용하기.
2. 주어진 num 만큼만 한수 계산하기.
"""


from bisect import bisect_left, bisect_right

N = int(input())
han_num = []

for i in range(1, 1000): #1000은 등차 수열이 만족하지 않기 때문에 제외
    if i <= 99:
        han_num.append(i)
        continue
    str_i = str(i)
    dif_1 = int(str_i[0]) - int(str_i[1])
    dif_2 = int(str_i[1]) - int(str_i[-1])
    if dif_1 == dif_2:
        han_num.append(i)
        
print(bisect_right(han_num, N))


"""
N = int(input())
cnt = 0

for i in range(1, N + 1):
    if i <= 99:
        cnt += 1
        continue
    num = list(map(int, str(i))) # 자리수 분리
    if num[0] - num[1] == num[1] - num[2]:
        cnt += 1

print(cnt)
"""