"""
대각선 : 1 -> 2 -> 3 -> 4 -> ...
"""

X = int(input())
S = 0
S_list = []
n = 0

while X > S:
    n += 1
    S += n
    S_list.append(S)

if X == 1:
    print("1/1")
    
elif n % 2 == 1: #홀수
    print(f'{S_list[-1] -X + 1}/{X - S_list[-2]}')
    
elif n % 2 == 0: #짝수
    print(f'{X - S_list[-2]}/{S_list[-1] - X + 1}')
    

