A, B = map(str, input().split())
A_new, B_new = 0, 0
digit_num = 2

for i, j in zip(A[::-1], B[::-1]):
    A_new += (int(i) * 10 ** digit_num)
    B_new += (int(j) * 10 ** digit_num)
    digit_num -= 1

print(A_new) if A_new > B_new else print(B_new)
    