depths = open("depth.txt")
window1 = [3]

window1.append(int(next(depths)))
window1.append(int(next(depths)))
window1.append(int(next(depths)))
w1val = window1[0] + window1[1] + window1[2]
inc = 0
while True:
    try:
        window1[0] = window1[1]
        window1[1] = window1[2]
        window1[2] = int(next(depths))
        w2val = window1[0] + window1[1] + window1[2]
        if w2val > w1val:
            inc = inc + 1
        w1val = w2val
    except:
        break
print(inc)