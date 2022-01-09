"""
국영수 : sorted에서 multiple keys 활용하려면 tuple로 묶는다. 이때, -를 붙이면 내림차순, +면 오름차순이다.
"""
n = int(input())

info_list = []

for _ in range(n):
    name, kor, eng, math = input().split()
    
    info_list.append([name, int(kor), int(eng), int(math)])

# 국어 감소하는 순서
info_list = sorted(info_list, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for info in info_list:
    print(info[0])
    


