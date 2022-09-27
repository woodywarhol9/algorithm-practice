import re

def solution(new_id):
    # 대문자 -> 소문자
    new_id = new_id.lower()
    # 허용되는 문자만 받아오기
    new_id = re.sub(r"[^0-9a-z-_.]", "", new_id)
    # .는 그대로 쓰면 문자 전체가 됨
    new_id = re.sub(r"[.]+", ".", new_id)
    new_id = re.sub("^[.]|[.]$", "", new_id)
    # 길이 0 처리
    if not len(new_id):
        new_id = "a"
    # 길이 16 이상 처리
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = re.sub(r"[.]$", "", new_id)
    else:
        while True:
            if len(new_id) <= 2:
                new_id += new_id[-1]
            else:
                break
            
    return new_id