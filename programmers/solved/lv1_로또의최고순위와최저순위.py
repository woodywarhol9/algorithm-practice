def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5}
    answer = [0, 0]
    
    correct = len(set(lottos) & set(win_nums))
    bonus = lottos.count(0)
    
    answer[0] = 6 if (correct + bonus) not in rank else rank[correct + bonus]
    answer[1] = 6 if correct not in rank else rank[correct]
    
    return answer