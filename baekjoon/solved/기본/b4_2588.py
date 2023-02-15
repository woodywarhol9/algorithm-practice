num1 = int(input())
num2 = int(input())

str1 = str(num1)
str2 = str(num2)

num3 = num1 * int(str2[2])
num4 = num1 * int(str2[1])
num5 = num1 * int(str2[0])

print(num3)
print(num4)
print(num5)
print(num3 + num4 * 10 + num5 * 100)