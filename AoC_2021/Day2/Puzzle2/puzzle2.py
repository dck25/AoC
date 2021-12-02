path = open("input.txt")
h = 0
aim = 0
d = 0

while True:
    try:
        print(h)
        command = next(path)
        direction = command.split(" ")[0]
        magnitude = int(command.split(" ")[1])

        if direction == "forward":
            h = h + magnitude
            d = d + (magnitude*aim)
        elif direction == "down":
            aim = aim + magnitude
        else:
            aim = aim - magnitude
    except:
        break

print(d)
print(h)
print(aim)
print(h*d)