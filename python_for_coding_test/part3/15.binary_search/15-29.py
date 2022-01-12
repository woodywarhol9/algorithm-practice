"""
공유기 설치 : 
"""
n, c  = map(int, input().split())
num_list = []
for _ in range(n):
    num_list.append(int(input()))

sorted_list = sorted(num_list)
print(sorted_list)