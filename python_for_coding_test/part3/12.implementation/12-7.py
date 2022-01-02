"""
럭키 스트레이트 : 숫자를 절반으로 나눴을 때의 합이 같다면 LUCKY, 다르다면 READY 출력
"""
N = int(input())
N_str = str(N)

#쪼개기
left = N_str[:len(N_str)//2]
right = N_str[len(N_str)//2:]
#합 구하기
left_sum = sum([int(x) for x in left])
right_sum = sum([int(x) for x in right])

print("LUCKY" if left_sum == right_sum else "READY")