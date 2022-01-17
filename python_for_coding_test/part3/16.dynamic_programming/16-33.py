"""
퇴사 : 
"""
n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는 데 걸리는 시간
dp = [] # 각 상담을 완료했을 때 받을 수 있는 금액

for _ in range(n):
    dp.append(list(map(int, input().split())))