test_case = int(input())

for _ in range(test_case):
    height, width, n = map(int, input().split())
    # n이 height의 배수일 경우
    if n % height == 0:
        order = n // height
        floor = height
    else:
        order, floor = divmod(n, height)
        order += 1
    print(f'{floor*100+order}')


