def solution(seoul):
    idx = 0
    for i, name in enumerate(seoul):
        if name == "Kim":
            idx = i
            break
    
    return f"김서방은 {idx}에 있다"


"""
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
"""