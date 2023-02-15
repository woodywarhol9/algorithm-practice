T = int(input())

for _ in range(T):
    R, S = input().split()
    for char in S:
        print(char*int(R), end ="")
    print("")