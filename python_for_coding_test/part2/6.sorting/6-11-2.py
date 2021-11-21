"""
아이디어
- 10만 이하의 양의 정수라서 기본 정렬 혹은 계수 정렬 사용 가능. 
- key 활용해서 성적 순으로 정렬 후 이름 출력 
"""

#계수 정렬
n = 2

array = [("홍길동",95),("이순신",77)]
name = []
score = []

for i in array:
    name.append(i[0])
    score.append(i[1])
     
count = [0] * (max(score) + 1)

for i in range(len(array)):
    count[array[i][1]] += 1 # 각 데이터에 해당하는 인덱서의 값 증가'

for i in range(len(count)):
    for j in range(count[i]): #count 개수 만큼 출력
        idx = score.index(i)
        print(name[idx])
