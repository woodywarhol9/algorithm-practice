"""
아이디어 : i - 1 번째 식량 창고 털기 vs i - 2 번째 + i 번째 식량 창고 털기
"""
n = 4
#식량 정보
array = [1, 3, 1, 5]

#DP 테이블 초기화(최대 식량 창고 개수 N개)
d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1]) #털지 말지 결정
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])