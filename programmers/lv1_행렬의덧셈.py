def solution(arr1, arr2):
    # 전개 순서 : [[1, 2], [2, 3]] // [[3,4], [5,6]] => [1,2], [3,4] => [4, 6]
    result = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return result
    