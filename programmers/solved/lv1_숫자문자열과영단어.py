def solution(s):
    num = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
    eng_num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    eng_dict = dict(zip(eng_num, num))
    
    temp = "" # 임시 문자열 저장
    answer = ""
    
    for i in s:
        if i in num:
            answer += i
        else:
            temp += i
        if temp in eng_num:
            answer += eng_dict[temp]
            temp = ""
            
    return int(answer)