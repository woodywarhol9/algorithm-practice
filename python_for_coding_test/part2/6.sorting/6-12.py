"""
아이디어
- K번 동안 배열 A의 가장 작은 원소와 배열 B의 가장 큰 원소와 교체. 
- 교체하기 전 원소끼리 크기 비교 필요.
"""

n, k = map(int, input().split())
a = list(map(int, input().split())) #배열 A 입력
b = list(map(int, input().split())) #배열 B 입력

#A는 오름차, B는 내림차 정렬해 0번째 부터 비교 후 교체
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        #원소 교체
        a[i], b[i] = b[i], a[i]
    else: #가장 큰 값보다 가장 작은 값이 클 경우 더 볼 필요 없으므로 break
        break

print(sum(a))