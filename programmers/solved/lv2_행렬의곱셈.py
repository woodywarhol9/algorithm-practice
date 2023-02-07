# (a x b) * (b x a) = (a x a)
# 행렬의 곱 : 행 - 열 성분 사이 곱
def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))]for _ in range(len(arr1))]
    for i, row in enumerate(arr1):
        # zip(*arr2)를 사용해서, 행 - 열 전환 -> 행과 열이 곱해질 수 있도록!
        for j, col in enumerate(zip(*arr2)):
            # 행 - 열 사이 곱
            answer[i][j] = sum([row[k] * col[k] for k in range(len(col))])
            
    return answer