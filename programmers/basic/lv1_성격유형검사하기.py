def solution(survey, choices):
    # 미리 알파벳 순으로 정렬
    answer = ["R", "C", "J", "A"]
    score = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N": 0}
    
    for s, c in zip(survey, choices):
        if c < 4:
            score[s[0]] += (4 - c)
        elif c > 4:
            score[s[1]] += (c - 4)
            
    if score["R"] < score["T"]:
        answer[0] = "T"
        
    if score["C"] < score["F"]:
        answer[1] = "F"
        
    if score["J"] < score["M"]:
        answer[2] = "M"
        
    if score["A"] < score["N"]:
        answer[3] = "N"
    
    return "".join(answer)