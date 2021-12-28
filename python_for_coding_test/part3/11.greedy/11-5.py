"""
볼링공 고르기 : K개의 공 번호를 정렬 후 순회하자. 이때 unique 값을 설정해 unique 값의 경우 case_num에 포함 안 시킨다.
"""


N, M = map(int, input().split())
K = sorted(list(map(int, input().split())))

count = 0
case_num = 0

for i in K:
    unique = i
    count += 1
    for j in K[count:]:
        if j == unique:
            continue
        else:
            case_num += 1
    
print(case_num)