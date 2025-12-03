with open('./input.txt', 'r') as file:
    banks = [line.rstrip('\n') for line in file]

output_joltage = 0

# part 1
for joltage in banks:
    max = ('0', '0')
    
    for digit in range(len(joltage)):
        for val in range(digit + 1, len(joltage)):
            first_battery, second_battery = joltage[digit], joltage[val]
            if (first_battery, second_battery) > max:
                max = (first_battery, second_battery)
    
    output_joltage += int(max[0] + max[1]) 

print(output_joltage)

            

