def solution(prices):
    # 초기값 : 가격이 떨어지지 않는다고 가정한 경우
    answer = [i for i in range(len(prices) -1, -1, -1)]
    # 시간 저장
    time = []
    for i, price in enumerate(prices):
        # 가격이 떨어진 경우
        while time and prices[time[-1]] > price:
            j = time.pop()
            # 시작부터 떨어지기 전까지 걸린 시간
            answer[j] = i - j
        # 입력 시작
        time.append(i)
    
    return answer