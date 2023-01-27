from bisect import bisect_right

def solution(d, budget):
    d.sort()
    cum_sum = []
    
    pre_sum = 0
    # 누적 합 계산
    for i in range(len(d)):
        pre_sum += d[i]
        cum_sum.append(pre_sum)
        
    return bisect_right(cum_sum, budget)