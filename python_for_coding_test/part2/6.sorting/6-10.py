"""
아이디어 : 기본 정렬 라이브러리를 활용할 수 있는 지
"""

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))
    
array = sorted(array, reverse = True) #기본으론 오름차순이기 때문에 reverse 필요

for i in array:
    print(i, end = " ")