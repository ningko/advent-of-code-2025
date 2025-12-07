with open('./input.txt', 'r') as file:
    arr = [line.rstrip('\n') for line in file]

matrix = [list(row) for row in arr]
rows = len(matrix)
cols = len(matrix[0])

start_col = None
start_row = None
splits = 0

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == 'S':
            start_row = r
            start_col = c
            break
    if start_col is not None:
        break

active = {start_col}

for r in range(start_row + 1, rows):
    next_active = set()

    for c in active:
        if c < 0 or c >= cols:
            continue
        
        cell = matrix[r][c]
        if cell == '^':
            splits += 1
            if c - 1 >= 0:
                next_active.add(c - 1)
            if c + 1 < cols:
                next_active.add(c + 1)
        else:
            next_active.add(c)
    active = next_active

    if not active:
        break

print(splits)