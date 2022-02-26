N = int(input())
sum = 1
count = 0

while True:
    if (N - sum) <= 0:
        print(count + 1)
        break
    count += 1
    sum += (count * 6)

    