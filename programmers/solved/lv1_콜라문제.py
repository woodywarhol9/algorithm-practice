# 몫 : 새로 받을 콜라 개수, 나머지 : 남은 콜라 개수
def solution(a, b, n):
    answer = 0
    # 교환 가능할 때 까지 실행
    while n >= a:
        q, r = divmod(n, a)
        # 교환 비가 1보다 큰 경우
        q *= b
        # 받은 콜라 개수 추가
        answer += q
        # 현재 콜라 개수 갱신
        n = q + r
    return answer