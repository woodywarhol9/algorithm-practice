def solution(numbers):
    # 문자로 접근하기 위해서 형 변환
    numbers = list(map(str, numbers))
    # 비교를 위해서 4글자로 맞춰주기
    numbers.sort(key = lambda x : (x * 4)[:4], reverse = True)
    answer = int("".join(numbers))
    
    return str(answer)