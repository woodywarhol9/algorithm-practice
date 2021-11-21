"""
아이디어
- 10만 이하의 양의 정수라서 기본 정렬 혹은 계수 정렬 사용 가능. 
- key 활용해서 성적 순으로 정렬 후 이름 출력 
"""

#기본 정렬
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    #이름은 str, 성적은 int
    array.append((input_data[0], int(input_data[1])))

#key를 이용해 정렬
array = sorted(array, key = lambda student : student[1])

for student in array:
    print(student[0], end = " ")

