import sys

speed = list(map(int, input().split()))
asc = 0
dsc = 0
for i in range(8):
    if speed[i] == i + 1:
        continue
    else:
        break
else:
    asc = 1

for i in range(8):
    if speed[i] == 8 - i:
        continue
    else:
        break
else:
    dsc = 1

if asc == 1:
    print("ascending")
elif dsc == 1:
    print("descending")
else:
    print("mixed")