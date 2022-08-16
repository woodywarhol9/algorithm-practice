def solution(x):
    x_str = str(x)
    sum_temp = 0
    
    for i in x_str:
        sum_temp += int(i)
    
    flag = True if x % sum_temp == 0 else False
    return flag

"""
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0
"""