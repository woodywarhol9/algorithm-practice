def get_num(k, min):
    if k == m:
        print(*num_list)
        return
    # 최소 값을 전달
    for i in range(min, n + 1):
        num_list[k] = i
        get_num(k + 1, i)
    
def solution():
    global n
    global m
    n, m = map(int, input().split())
    # 수열
    global num_list
    num_list = [0] * m
    # 탐색 시작
    get_num(0, 1)
    

solution()