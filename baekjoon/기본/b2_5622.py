"""
S와 U만 따로 뺴주면 나머진 3의 배수로 처리 가능
=> YZ를 생각 안 했었다... 
"""

word = input()
count = 0

char_list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

for i in word:
    for c in char_list:
        if i in c:
            count += (3 + char_list.index(c))     
        
print(count)