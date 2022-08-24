from collections import Counter

def solution(participant, completion):
    p_list = Counter(participant)
    c_list = Counter(completion)
    
    result = list(map(lambda x : x, p_list - c_list))[0]
    
    return result