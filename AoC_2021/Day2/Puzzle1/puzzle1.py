path = open("input.txt")
h = 0
d = 0

while True:
    try:
        command = next(path)
        direction = command.split(" ")[0]
        magnitude = int(command.split(" ")[1])

        if direction == "forward":
            h = h + magnitude
        elif direction == "down":
            d = d + magnitude
        else:
            d = d - magnitude
    except:
        break

print(d*h)