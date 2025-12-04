with open('./input.txt', 'r') as file:
    arr = [line.rstrip('\n') for line in file]

matrix = [list(row) for row in arr]
rows = len(matrix)
cols = len(matrix[0])
adjacent_positions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
accessible_rolls = 0

for element in arr:
    matrix.append(list(element))

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == '@':
            adyacent_rolls = 0
            for x, y in adjacent_positions:
                r = i + x
                c = j + y
                if 0 <= r < rows and 0 <= c < cols:
                    if matrix[r][c] == '@':
                        adyacent_rolls += 1
            
            if adyacent_rolls <= 3:
                accessible_rolls += 1

print(accessible_rolls)