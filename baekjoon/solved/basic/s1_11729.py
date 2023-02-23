"""
n에서의 하노이 탑
1. n - 1 탑을 2번째(idx 1)위치로 옮김
2. n번째 층을 3번째(idx 2)위치로 옮김
3. 3번째 위치(idx 2) 위치에 다시 n - 1 탑을 쌓음. 
"""
def hanoi(n : int, start : int, end : int):
    # start, end가 아닌 위치
    mid = 3 - (start + end)
    if n == 1:
        print(start + 1, end + 1)
        return
    
    hanoi(n - 1, start, mid)
    print(start + 1, end + 1)
    hanoi(n - 1, mid, end)    
        
n = int(input())
print(2**n - 1)
hanoi(n, 0, 2)