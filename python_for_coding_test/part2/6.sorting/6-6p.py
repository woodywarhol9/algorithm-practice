"""
계수 정렬 : 모든 범위를 포함하는 리스트를 선언해 처리. 이때 모든 원소가 양의 정수여야 한다. 
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
#모든 범위를 포함하는 리스트 선언
count = [0] * (max(array) + 1) #K는 최댓값!

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱서의 값 증가

for i in range(len(count)):
    for j in range(count[i]): #count 개수 만큼 출력
        print(i, end = " ")
    