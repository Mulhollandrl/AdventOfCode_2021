file = open("data.txt")
data = file.readlines()
file.close()

def partOne(start, data):
    x = start
    y = start

    for line in data:
        splitLine = line.split()

        command = splitLine[0]
        amount = int(splitLine[1])

        if command == "forward":
            x += amount
        elif command == "down":
            y += amount
        else:
            y -= amount

    return x*y

def partTwo(start, data):
    x = start
    y = start
    aim = start

    for line in data:
        splitLine = line.split()

        command = splitLine[0]
        amount = int(splitLine[1])

        if command == "forward":
            x += amount
            y += amount * aim
        elif command == "down":
            aim += amount
        else:
            aim -= amount

    return x * y

print(f"The position after the moves in the first problem is {partOne(0,data)}!")
print(f"The position after the moves in the second problem is {partTwo(0,data)}!")
