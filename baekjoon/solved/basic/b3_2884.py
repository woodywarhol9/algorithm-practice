H, M =  map(int, input().split)
time = 60 * H + M

alarm = time - 45
if alarm >= 0:
    print(alarm // 60, alarm % 60)
else:
    new_alarm = 24 * 60 + alarm
    print(new_alarm // 60, new_alarm % 60)
