from bisect import bisect_left, bisect_right

def solution(citations):
    citations.sort()
    # h ~ 0까지 가능
    cum_sum = dict(zip(range(len(citations)), [0] * len(citations)))
    # h보다 더 많이 인용된 논문 개수
    temp_sum = sum([1 for i in citations if i > len(citations)])
    for h in range(len(citations), -1, -1):
        right_idx = bisect_right(citations, h)     
        left_idx = bisect_left(citations, h)
        
        temp_sum += (right_idx - left_idx)
        # 최대 인용 순간
        if h <= temp_sum:
            break
        
    return h