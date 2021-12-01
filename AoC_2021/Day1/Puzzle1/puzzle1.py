depths = open("depth.txt")
inc=0
cur_depth = int(next(depths))

while True:
    try:
        next_depth = int(next(depths))
        if cur_depth < next_depth:
            inc=inc+1
        cur_depth = next_depth
    except:
        break    
print(inc)
