N = int(input())

count_2 = 0
count_5 = 0
for i in range(1, N + 1):
    # 약수로 2, 5를 가지지 않는 경우
    if i % 2 != 0 and i % 5 !=0:
        continue
    # 약수로 5를 가지는 경우 처리
    if i % 5 == 0:
        while i % 5 == 0:
            i //= 5
            count_5 += 1
    # 약수로 2를 가지는 경우 처리
    if i % 2 == 0:
        while i % 2 == 0:
            i //= 2
            count_2 += 1

if count_2 and count_5:
    print(min(count_2, count_5))
else:
    print(0)