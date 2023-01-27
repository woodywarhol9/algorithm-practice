def solution(answers):
    # 정답지
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    p_sol = [0, 0, 0]
    
    for i, sol in enumerate(answers):
        if sol == p1[i % 5]:
            p_sol[0] += 1
        if sol == p2[i % 8]:
            p_sol[1] += 1
        if sol == p3[i % 10]:
            p_sol[2] += 1
    
    return [i + 1 for i in range(3) if (p_sol[i] == max(p_sol)) and (p_sol[i] != 0)]