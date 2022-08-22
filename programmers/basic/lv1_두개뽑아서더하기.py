def solution(numbers):
    sum_list = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            sum_list.add(numbers[i] + numbers[j])
    
    return sorted(sum_list)