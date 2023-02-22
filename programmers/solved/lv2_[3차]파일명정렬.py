# 파일명에 포함된 숫자를 반영한 정렬 기능 구현
# 숫자 : 0 ~ 99999 -> 숫자 앞의 0은 무시
# 정렬 기준 : 1. HEAD 2.NUMBER 3. 입력 순으로

# NUMBER의 숫자와, Tail의 숫자 구분 필요
import re

def solution(files):
    # (HEAD)(NUMBER)(TAIL) 분리
    pt = r"([^\d]+)(\d+)(.*)"
    # HEAD - NUMBER -TAIL 분리 후 새로운 파일명
    file_splited = []
    for file in files:
        obj = re.search(pt, file)
        file_splited.append([obj.group(1), obj.group(2), obj.group(3)])
    # Number 부분 정렬할 때, int로 변경하지 않으면 10 > 2가 됨
    # int : 앞의 0을 알아서 없애줌
    # str.lstrip("0")은 "0"이 문제 번호인 경우 에러 발생
    file_splited.sort(key = lambda x : (x[0].lower(), int(x[1])))
    file_splited = ["".join(file) for file in file_splited]
    
    return file_splited