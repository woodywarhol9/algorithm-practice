# 10 이상 부터는, 한 자리씩 말하기!
# 자신이 말해야할 번호만 출력하면 됨

# n 진법으로 변환하기
def get_nbase(n: int, i: int) -> str:
    nbase = ""
    over_10 = {10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}
    while i:
        q, r = divmod(i, n)
        # 초기화
        i = q
        if r in over_10:
            r = over_10[r]
        nbase += str(r)
    return nbase[::-1]
        
def solution(n, t, m, p):
    # 튜브의 대답
    answer_list = []
    # n 진법 정보
    nbase_list = ["0"]
    # 미리 n진법 숫자 구해두기
    for i in range(1, t * m):
        nbase_list.append(get_nbase(n, i))
    # N 진수 게임 시작
    cnt = 0
    for num in nbase_list:
        # 1 글자씩
        for digit in num:
            # 튜브 순서일 경우
            if cnt % m == p - 1:
                answer_list.append(digit)
            cnt += 1
            # 게임 끝
            if cnt >= t * m:
                break
        if cnt >= t * m:
            break
            
    return "".join(answer_list)