"""
일반식을 재귀 함수로 구현하기.
1. 시간 초과 발생.
2. memoization시도. => 성공.
"""
def recursive(floor, number):
    # 일반식 구하기 + memoization
    if (floor, number) in memo:
        return memo[(floor, number)]
    
    if number == 1:
        memo[(floor, number)] = 1
        return 1
    
    elif floor == 0 :
        memo[(floor, number)] = int(number)
        return int(number)
    
    else :
        sum = 0
        for i in range(1, number + 1):
            temp = recursive(floor -1, i)
            memo[(floor - 1, i)] = temp
            sum += temp
         
        return sum
            
test_case = int(input())
memo = {}

for _ in range(test_case):
    floor = int(input())
    number = int(input())
    # 전 층의 합 구하기.
    sum = recursive(floor, number)
    print(sum)
    