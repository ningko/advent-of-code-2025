with open('./input.txt', 'r') as file:
    arr = file.read().split(',')
    
ran = [element.split('-') for element in arr]
int_range = []

for i in ran:
    int_range.append([int(j) for j in i])

invalid_id = 0

# part 1
for element in int_range:
    val_1 = element[0]
    val_2 = element[1]
    for _ in range(val_1, val_2 + 1):
        id = _
        string_id = str(id)
        first_half = string_id[:len(string_id)//2]
        second_half = string_id[len(string_id)//2:]

        if first_half == second_half:
            invalid_id += int(first_half + second_half)

print(invalid_id)

