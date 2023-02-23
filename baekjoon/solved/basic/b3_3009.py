row_count = {}
col_count = {}

for _ in range(3):
    n , m  = map(int, input().split())
    if n not in row_count:
        row_count[n] = 0
    if m not in col_count:
        col_count[m] = 0 
    row_count[n] += 1
    col_count[m] += 1

row, col = min(row_count, key = row_count.get), min(col_count, key = col_count.get)
print(row, col)
