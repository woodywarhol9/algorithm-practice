"""
곱하기 혹은 더하기 : 숫자가 0일 경우에만 더하기 처리하고 나머지는 곱하기 처리한다. 이때 초기 값 0임을 처리하기 위해서 max == 0 조건을 추가했다.
"""
S = input()

max = 0
count = 0

for i in S:
    i = int(i)   
    if i == 0 or max == 0: 
        max += i
    else :
        max *= i

print(max)
    