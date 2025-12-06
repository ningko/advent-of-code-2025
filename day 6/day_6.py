with open('./input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

width = max(len(line) for line in lines)
grid = [line.ljust(width) for line in lines]

spans = []
in_span = False
start = None

for col in range(width):
    col_has_char = any(grid[row][col] != ' ' for row in range(len(grid)))
    if col_has_char:
        if not in_span:
            in_span = True
            start = col
    else:
        if in_span:
            spans.append((start, col))
            in_span = False

if in_span:
    spans.append((start, width))

problems = []

for s, e in spans:
    nums = []
    valid = True

    for row in range(4):
        block = grid[row][s:e].strip()
        if not block:
            valid = False
            break
        if not block.isdigit():
            valid = False
            break
        nums.append((int(block)))
    
    operator = grid[4][s:e].strip()
    if operator not in ('+', '*'):
        valid = False
    
    if not valid:
        continue

    problems.append((nums, operator))

total = 0

for nums, operator in problems:
    if operator == '+':
        value = sum(nums)
    else:
        value = 1
        for n in nums:
            value *= n

    total += value

print(total)
