def get_num(k):
    # 수열이 완성된 경우
    if k == m:
        print(*num_list)
        return
    # 수열에 원소 저장
    for i in range(1, n + 1):
            num_list[k] = i
            get_num(k + 1)
                    
def solution(n, m):
    # 현재 수열
    global num_list
    num_list = [0] * m
    get_num(0)
    
n, m = map(int, input().split())
solution(n, m)