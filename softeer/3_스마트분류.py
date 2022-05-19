import sys

line_len, robot_range = map(int, input().split())
line_info = list(input())

count = 0
for idx, obj in enumerate(line_info):
    if obj == "P":
        for j in range(idx - robot_range, idx + robot_range + 1):
            if j < 0 or j > line_len - 1:
                continue
            elif line_info[j] == "H":
                count += 1
                line_info[j] = 0
                break
print(count)