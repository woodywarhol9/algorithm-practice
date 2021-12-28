"""
문자열 뒤집기 : 0과 1 중 더 많은 수를 기준으로 뒤집는다. 이어진 수가 없다는 가정 하에 최대 뒤집기 횟수를 지정한다. 최종적으로 이어진 수의 개수만큼 뒤집기 횟수를 줄여준다.
"""
S = input()

count_0, count_1 = S.count("0"), S.count("1")

is_series = 0 #초기 조건
reverse_count = min(count_0, count_1)

for i in S:
    i = int(i)
    
    if count_0 >= count_1:
        if i == 1 :
            is_series += 1
        
        elif i == 0 and is_series != 0: #is_series 처리
            reverse_count -= (is_series - 1)
            is_series = 0
    
    else :
        if i == 0 :
            is_series += 1
        
        elif i == 1 and is_series != 0:
            reverse_count -= (is_series - 1)
            is_series = 0

print(reverse_count)
