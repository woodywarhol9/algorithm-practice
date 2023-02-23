"""
중복 처리할 때 set 활용하기.
"""
num = set(range(1, 10001))
c_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    c_num.add(i)
    
self_num = sorted(num - c_num)
for i in self_num:
    print(i)