def solution(ingredient):
    answer = 0
    # stack 활용
    food = []
    for i in ingredient:
        food.append(i)
        if food[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                food.pop()
    return answer
# 시간 초과 발생한 풀이
"""
def solution(ingredient):
    answer = 0
    
    food = list(map(str, ingredient))
    food = "".join(food)
    while food:
        temp = food.replace("1231", "", 1)
        if food == temp:
            break
        answer += 1
        food = temp
    return answer
"""
# 수정 풀이 -> 테스트 케이스 통과 실패
# 따로 옮겨 포장한다고 돼 있음 -> 한번에 1개만 가능 -> 테스트 케이스도 이와 관련 있을 것...
"""
def solution(ingredient):
    answer = 0
    
    food = list(map(str, ingredient))
    food = "".join(food)
    while food:
        temp = food.replace("1231", "")
        if food == temp:
            break
        # 포장한 햄버거 개수
        answer += (len(food) - len(temp)) // 4
        food = temp
    return answer
"""