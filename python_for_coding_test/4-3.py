'''
아이디어 : 체스 판에서의 위치를 행은 숫자, 열은 문자로 표현한다.

input : a1 형태
'''

#현재 위치
input_data = input() #str
row = int(input_data[1]) 
col = int(ord(input_data[0])) - int(ord("a")) + 1 # 1~8

#8가지 방향
steps = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]

case_num = 0
for step in steps:
    
    next_row = row + step[0]
    next_col = col + step[1]
    
    #어느 방향이라도 만족 못하면 못 움직임
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        case_num += 1
        
print(case_num)