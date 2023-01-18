# -> 물 <-
# 짝수 개수로만 설정
def solution(food):
    half_lst = [(food[i] // 2) * str(i) for i in range(1, len(food))]
    half_lst = "".join(half_lst)
    answer = half_lst + "0" + half_lst[::-1]
    return answer