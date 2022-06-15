def fib(n):
    global count_fib
    count_fib += 1
    if n == 1 or n == 2:
        count_fib -= 1
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))

dp = {1 : 1, 2 : 1}
def fib_dp(n):
    global count_dp
    # n이 dp table에 있는 경우
    if n in dp:
        return dp[n]
    # n이 dp table에 없는 경우
    else:
        dp[n] = fib_dp(n - 1) + fib_dp(n  - 2)
        count_dp += 1
        return dp[n]
    
n = int(input())
count_fib, count_dp = 0, 0
fib(n)
fib_dp(n)
# count_fib에 1, 2
print(count_fib + 1, count_dp)