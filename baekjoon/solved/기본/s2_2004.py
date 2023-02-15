n, m = map(int, input().split())

def count_five(n):
    count = 0
    while n != 0:
        n //= 5
        count += n
    return count

def count_two(n):
    count = 0
    while n != 0:
        n //= 2
        count += n
    return count
# n, m, n - m에 대한 5, 2 개수 구하기
n_five, n_two = count_five(n), count_two(n)
m_five, m_two = count_five(m), count_two(m)
nm_five, nm_two = count_five(n-m), count_two(n-m)

total_zero = min((n_five - m_five - nm_five), (n_two - m_two - nm_two))
print(total_zero)