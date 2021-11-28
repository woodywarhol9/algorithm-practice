"""
아이디어 : 
"""
n, m = map(int, input().split())
# N개의 화폐 단위 정보 입력
array = []
for i in range(n):
    array.append(int(input()))
    
#DP 테이블 초기화
d = [10001] * (m + 1) 

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] =  min(d[j], d[j - array[i]] + 1) 

#계산 결과 출력
if d[m] == 10001: #M원을 만드는 방법이 없을 경우
    print(-1)

else:
    print(d[m])
            