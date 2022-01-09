"""
안테나 : 성분 간 연산을 할 수 있도록 Numpy array로 변경 후 처리. 이때 Numpy array를 반복시키려면 nditer 사용!
"""

#1. Numpy로 풀이
import numpy as np

n = int(input())
house_np = np.array(list(map(int, input().split())))
len_list = []

for i in np.nditer(house_np):
    len_list.append(sum(abs(house_np - i)))

min_value = min(len_list)
min_index = len_list.index(min_value)
print(house_np[min_index])


# 2. List로 풀이
n = int(input())
house_list = list(map(int, input().split()))
len_list = []

for i in house_list:
    temp_list = [i] * n
    dif = [abs(x - y) for x, y in zip(temp_list, house_list)]
    len_list.append(sum(dif))

min_value = min(len_list)
min_index = len_list.index(min_value)
print(house_list[min_index])