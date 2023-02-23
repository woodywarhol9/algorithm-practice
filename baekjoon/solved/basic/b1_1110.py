"""
형변환해서 찾을 수도 있고 몫, 나머지 이용해서 찾을 수도 있다!
"""

N = int(input())
num = N
cycle = 0

while True:
    if num < 10:
        num = 10 * num + num
    else:
        num_temp = int(str(num)[0])+int(str(num)[1])
        num = 10 * int(str(num)[1]) + int(num_temp%10)
   
    cycle += 1
    if N == num:
        break

print(cycle)
    

    
    