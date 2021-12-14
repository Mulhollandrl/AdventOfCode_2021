file = open("data.txt")
data = file.readlines()
file.close()

increases = 0


def partOne(increases, data):
    for i in range(len(data) - 1):
        firstLine = int(data[i])
        secondLine = int(data[i + 1])

        if secondLine > firstLine:
            increases += 1

    return increases


def partTwo(increases, data):
    for i in range(len(data) - 3):
        firstSum = int(data[i])
        firstSum += int(data[i + 1])
        firstSum += int(data[i + 2])

        secondSum = int(data[i + 1])
        secondSum += int(data[i + 2])
        secondSum += int(data[i + 3])

        if secondSum > firstSum:
            increases += 1

    return increases

def dude(data):
    for i in range(len(data) - 3):
        sum = int(data[i])
        sum += int(data[i+1])
        sum += int(data[i+2])

        print(sum)

dude(data)
print(partOne(increases, data))
print(partTwo(increases, data))

