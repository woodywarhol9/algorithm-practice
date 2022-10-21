def get_num(k):
    # 수열이 완성된 경우
    if k == m:
        print(*num_list)
        return
    # 수열에 원소 저장
    for i in range(1, n + 1):
        if not isused[i]:
            num_list[k] = i
            isused[i] = 1
            get_num(k + 1)
            # 사용 후 제거
            isused[i] = 0
                    
def solution(n, m):
    # 숫자 중복 여부 확인
    global isused
    isused = [0] * (n + 1)
    # 현재 수열
    global num_list
    num_list = [0] * m
    get_num(0)
    
n, m = map(int, input().split())
solution(n, m)