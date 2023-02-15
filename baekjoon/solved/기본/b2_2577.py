"""
list의 count 함수를 이용하는 방법도 있다.
"""

A = int(input())
B = int(input())
C = int(input())
result = A * B * C

count = [0] * (10)
for i in range(len(str(result))):
    count[result % 10] += 1
    result = result // 10

for num in count:
    print(num)
    
    
"""
A = int(input())
B = int(input())
C = int(input())

result = list(str(A*B*C))

for i in range(10):
    print(result.count(str(i)))

"""