# 0 1 2 3 4 5 6 7
# 0 1 2 3
# 0 1
def solution(n,a,b):
    # 1 라운드부터 시작하기 때문에
    answer = 1
    # 몫 정보로 대결 여부 파악할 수 있도록 변경
    # 몫이 같다면 둘이 매칭된 것
    a, b = a - 1, b - 1
    while a // 2 != b // 2:
        a //= 2
        b //= 2
        answer += 1
    return answer