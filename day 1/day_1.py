with open('./input.txt', 'r') as file:
    arr = [line.rstrip('\n') for line in file]

dial = 50
zeros = 0
clicks = 0

# part 1
for element in arr:
    turn = element[0]
    value = int(element[1:])

    if turn == "R":
        dial = (dial + value) % 100
        if dial == 0:
            zeros = zeros + 1
    elif turn == "L":
        dial = (dial - value) % 100
        if dial == 0:
            zeros = zeros + 1

print (zeros)

# part 2
dial = 50
for element in arr:
    turn = element[0]
    value = int(element[1:])

    if turn == "R":
        for _ in range(value):
            dial = (dial + 1) % 100
            if dial == 0:
                clicks = clicks + 1
    elif turn == "L":
        for _ in range(value):
            dial = (dial - 1) % 100
            if dial == 0:
                clicks = clicks + 1

print (clicks)