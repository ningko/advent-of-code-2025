with open('./input.txt', 'r') as file:
    banks = [line.rstrip('\n') for line in file]

output_joltage = 0
output_joltage_p2 = 0

# part 1
for joltage in banks:
    max_pair = ('0', '0')
    
    for digit in range(len(joltage)):
        for val in range(digit + 1, len(joltage)):
            first_battery, second_battery = joltage[digit], joltage[val]
            if (first_battery, second_battery) > max_pair:
                max_pair = (first_battery, second_battery)
    
    output_joltage += int(max_pair[0] + max_pair[1]) 
    
print(output_joltage)

# part 2
def max_twelve(num: str, i: int):
    remove = len(num) - i
    max_joltage = []

    for digit in num:
        while remove > 0 and max_joltage and max_joltage[-1] < digit:
            max_joltage.pop()
            remove -= 1
        max_joltage.append(digit)
    
    return ''.join(max_joltage[:i])

for joltage in banks:
    twelve = max_twelve(joltage, 12)
    output_joltage_p2 += int(twelve)

print(output_joltage_p2)



            

