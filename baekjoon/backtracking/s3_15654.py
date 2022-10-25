def backtrack(k):
    if k == m:
        print(*array)
        return
    for i in num_list:
        if not isused[i]:
            array[k] = i
            isused[i] = 1
            backtrack(k + 1)
            isused[i] = 0

def solution():
    global n
    global m
    n, m = map(int, input().split())
    # 수열
    global array
    array = [0] * m
    # 입력된 수
    global num_list
    global isused
    num_list = sorted(list(map(int, input().split())))
    isused = dict(zip(num_list, len(num_list) * [0]))
    backtrack(0)
    
solution()