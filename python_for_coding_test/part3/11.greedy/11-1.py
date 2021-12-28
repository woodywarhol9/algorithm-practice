"""
모험가 길드 : 그룹에 속한 인원 수보다 모험가의 공포도가 작거나 같을 때를 제외. 이때 공포를 기준으로 오름차순으로 회원을 정리 후 확인한다.
"""
N = int(input())
m = list(map(int, input().split()))
m_list = sorted(m)

count = 0
group_num = 0

for fear in m_list:
    count += 1
    if fear <= count:
        group_num += 1
        count = 0

print(group_num)
    
