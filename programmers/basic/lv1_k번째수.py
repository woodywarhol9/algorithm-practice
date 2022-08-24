def solution(array, commands):
    result = []
    for i, j, k in commands:
        result.append(sorted(array[i - 1: j])[k -1])
    return result
        