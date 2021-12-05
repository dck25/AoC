def expand_points(x1,x2,y1,y2,point_dict):
    if x1==x2:
        c1 = min(y1,y2)
        c2 = max(y1,y2)
        while int(c1) <= int(c2):
            key = str(x1) + "," + str(c1)
            if key in point_dict:
                point_dict[key] = point_dict[key] + 1
            else:
                point_dict[key] = 1
            c1 = int(c1) + 1
    elif y1==y2:
        c1 = min(x1,x2)
        c2 = max(x1,x2)
        while int(c1) <= int(c2):
            key = str(c1) + "," + str(y1)
            if key in point_dict:
                point_dict[key] = point_dict[key] + 1
            else:
                point_dict[key] = 1
            c1 = int(c1) + 1
    elif abs(x1-x2) == abs(y1-y2):
        if x1 > x2:
            x3 = -1
        else:
            x3 = 1
        if y1 > y2:
            y3 = -1
        else:
            y3 = 1
        while x1 != x2+x3 and y1 != y2+y3:
            key = str(x1) + "," + str(y1)
            if key in point_dict:
                point_dict[key] = point_dict[key] + 1
            else:
                point_dict[key] = 1
            x1 = x1 + x3
            y1 = y1 + y3

def load_points_hv():
    points = open("input.txt")
    point_dict = {}
    while True:
        try:
            line = next(points).split(" -> ")
            x1 = int(line[0].split(",")[0])
            x2 = int(line[1].split(",")[0])
            y1 = int(line[0].split(",")[1])
            y2 = int(line[1].split(",")[1].replace('\n',''))
            if x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2):
                expand_points(int(x1),int(x2),int(y1),int(y2),point_dict)
        except:
            break

    count = 0
    for c,v in point_dict.items():
        if v > 1:
            count = count + 1
    return count

print(load_points_hv())