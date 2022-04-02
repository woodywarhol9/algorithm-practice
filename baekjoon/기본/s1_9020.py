# 10000까지의 prime number 미리 구하기.
sieve = [True] * 10000
sieve[0] = False
m = 100

for i in range(2, m + 1):
    if sieve[i - 1] == True:
        for j in range(i + i, 10001, i):
            sieve[j - 1] = False


test_case = int(input())

for _ in range(test_case):
    n = int(input())
    
    # 확인할 시작, 끝점
    start = n // 2
    end = start
    
    for i in range(10001):
        if sieve[start - 1] and sieve[end - 1]:
            print(start, end)
            break
        start -= 1
        end += 1
    
        
            
        