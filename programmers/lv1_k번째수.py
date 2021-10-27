def solution(array, commands):
    answer = []
    
    #commands 접근
    for command in commands:
        i, j, k = command
        
        sorted_array = sorted(array[i-1:j]) #index 주의
        answer.append(sorted_array[k-1])
    
    return answer