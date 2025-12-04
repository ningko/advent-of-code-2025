with open('./input.txt', 'r') as file:
    arr = [line.rstrip('\n') for line in file]

matrix = [list(row) for row in arr]
rows = len(matrix)
cols = len(matrix[0])
adjacent_positions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
accessible_rolls = 0
removed_total = 0

# part 1
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == '@':
            adjacent_rolls = 0
            for x, y in adjacent_positions:
                r = i + x
                c = j + y
                if 0 <= r < rows and 0 <= c < cols:
                    if matrix[r][c] == '@':
                        adjacent_rolls += 1
            
            if adjacent_rolls <= 3:
                accessible_rolls += 1

print(accessible_rolls)

# part 2
while True:
    removable = []
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '@':
                adjacent_rolls = 0
                for x, y in adjacent_positions:
                    r = i + x
                    c = j + y
                    if 0 <= r < rows and 0 <= c < cols:
                        if matrix[r][c] == '@':
                            adjacent_rolls += 1
                
                if adjacent_rolls <= 3:
                    removable.append((i, j))
    if not removable:
        break

    for i, j in removable:
        matrix[i][j] = '.'

    removed_total += len(removable)

print(removed_total)