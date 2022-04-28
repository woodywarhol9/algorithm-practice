import sys

def parametric_search(array : list, target : int):
    start = 0
    end = len(array) - 1
    # 결과 저장
    result = 0
    
    while start <= end:
        mid = (start + end) // 2
        # 조건 만족시키기 위해서 start 이동
        if array[mid] < target:
            start = mid + 1
        # 조건 만족하는 최적 위치 찾기
        else:
            result = mid
            end = mid - 1        
    return result

        

array_len = int(input())
array = list(map(int,sys.stdin.readline().rstrip().split()))

# 증가 수열을 구성할 새로운 배열 생성
longest_array = [array[0]]
for i in array[1:]:
    last_num = longest_array[-1]
    # 새로 입력된 수가 더 큰 경우 바로 입력
    if i > last_num:
        longest_array.append(i)
    # 새로 입력된 수가 더 작을 경우 idx를 binary search를 통해서 구함.
    else:
        longest_array[parametric_search(longest_array, i)] = i
    
print(len(longest_array))