"""
괄호 변환 : 재귀로 구현하기. 재귀에 익숙해지자.
"""

# 올바른 괄호인지 판별
def is_correct(p):
    
    l_p_count = 0
    r_p_count = 0
    for c in p:
        if c == "(":
            l_p_count += 1    
        elif c == ")":
            r_p_count += 1
        if l_p_count < r_p_count:
            return False
    return True

def split(p):
    idx = 0
    l_p_count = 0
    r_p_count = 0
    
    u = ""
    v = ""
    # u, v 분리하기
    for c in p:
        idx += 1
        if c == "(":
            l_p_count += 1
        elif c == ")":
            r_p_count += 1
        if l_p_count == r_p_count:
            u = p[:idx]
            v = p[idx:]
            break
    return u, v

def solution(p):
    
    new_p = ""
    
    if len(p) == 0 or is_correct(p):
        return p
    
    u, v = split(p)
    # u가 올바른 괄호 문자열일 경우
    if is_correct(u):
        new_p = u + solution(v)
    # u가 올바른 괄호 문자열이 아닐 경우
    else:
        new_p += "("
        new_p += solution(v)
        new_p += ")"
        # 수정을 위해 list로 변경
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else :
                u[i] = "("
        
        new_p += "".join(u)
    
    return new_p
        
        
        
        

    

    
    
    
    
    