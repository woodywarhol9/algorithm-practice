def solution(n, arr1, arr2):
    arr1 = [list(f"{bin(i)[2:]:0>{n}}") for i in arr1]
    arr2 = [list(f"{bin(i)[2:]:0>{n}}") for i in arr2]
    
    decode = [[0] * n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            # 어느 한쪽에 벽이 존재하는 경우
            if int(arr1[row][col]) | int(arr2[row][col]):
                decode[row][col] = "#"
            # 양쪽 전부 벽에 없는 경우
            else:
                decode[row][col] = " "
        if col == n - 1:
            decode[row] = "".join(decode[row])
    
    return decode