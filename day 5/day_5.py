with open('./input.txt', 'r') as file:
    arr = [line.split('\n') for line in file.read().split('\n\n')]

first_arr = arr[0]
second_arr = arr[1]

ran = [element.split('-') for element in first_arr]

fresh_ids = []
available_ids = []

for i in ran:
    fresh_ids.append([int(j) for j in i])

for i in second_arr:
    available_ids.append(int(i))

fresh = 0
spoiled = 0

for available_id in available_ids:
    is_fresh = False

    for lo, hi in fresh_ids:
        if lo <= available_id <= hi:
            is_fresh = True
            break
    
    if is_fresh:
        fresh += 1
    else:
        spoiled += 1


print(fresh)
