with open('./input.txt', 'r') as file:
    arr = [line.rstrip('\n') for line in file]

matrix = [list(row) for row in arr]
rows = len(matrix)
cols = len(matrix[0])

start_col = None
start_row = None
splits = 0

# part 1
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

# part 2
active = {start_col: 1}

for r in range(start_row + 1, rows):
    if not active:
        break
    next_active = {}
    row = matrix[r]

    for c, count in active.items():
        if c < 0 or c >= cols:
            continue
        if row[c] == '^':
            if c - 1 >= 0:
                next_active[c - 1] = next_active.get(c - 1, 0) + count
            if c + 1 < cols:
                next_active[c + 1] = next_active.get(c + 1, 0) + count
        else:
            next_active[c] = next_active.get(c, 0) + count
    active = next_active

total_timelines = sum(active.values())

print(total_timelines)