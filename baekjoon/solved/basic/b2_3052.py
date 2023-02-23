remainder_list = []

for _ in range(10):
    num = int(input())
    remainder_list.append(num % 42)

print(len(set(remainder_list)))
    