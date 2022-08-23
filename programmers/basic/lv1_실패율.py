from collections import defaultdict, Counter

def solution(N, stages):
    # 현재 스테이지에 있거나 통과한 유저
    user_cnt_list = Counter(stages)
    rate_list = defaultdict(int)
    user_cnt = 0
    
    for i in range(N + 1, 0, -1):
        if i == N + 1:
            if i in user_cnt_list:
                user_cnt += user_cnt_list[i] 
            continue
        # 현재 스테이지에 있는 유저 추가
        if i in user_cnt_list:
            user_cnt += user_cnt_list[i]
        # 분모가 0인 경우 처리
        if user_cnt == 0:
            rate_list[i] = 0
            print(i)
            continue
        rate_list[i] = stages.count(i) / user_cnt
    
    result = sorted(rate_list.items(), key = lambda x : (-x[1], x[0]))
    result = list(map(lambda x : x[0], result))
    
    return result