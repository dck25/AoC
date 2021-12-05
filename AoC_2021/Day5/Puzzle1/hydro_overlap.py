

import json

def expand_points(x1,x2,y1,y2,point_dict):
    #print("called" + x1)
    if x1==x2:
        if y1 > y2: 
            c1 = y2
            c2 = y1
        else:
            c1 = y1
            c2 = y2
        while int(c1) <= int(c2):
            key = str(x1) + "," + str(c1)
            if key in point_dict:
                #print("increasing" + key)
                point_dict[key] = point_dict[key] + 1
            else:
                #print("adding " + key)
                point_dict[key] = 1
            c1 = int(c1) + 1
    elif y1==y2:
        #if y1 == 844:
        #    print(x1)
        #print("y match")
        if x1 > x2: 
            #print("x1 > x2")
            c1 = x2
            c2 = x1
        else:
            #print("else")
            c1 = x1
            c2 = x2
            #print(c1)
            #print(c2)
        while int(c1) <= int(c2):
            #print("while")
            key = str(c1) + "," + str(y1)
            if key in point_dict:
                #print("increasing" + key)
                point_dict[key] = point_dict[key] + 1
            else:
                #print("adding " + key)
                point_dict[key] = 1
            c1 = int(c1) + 1
            #print(c1)
    #print(key)
    #return point_dict


def load_points_hv():
    points = open("input.txt")
    point_dict = {}
    while True:
        try:
            line = next(points).split(" -> ")
            #print(line)
            x1 = line[0].split(",")[0]
            x2 = line[1].split(",")[0]
            y1 = line[0].split(",")[1]
            y2 = line[1].split(",")[1].replace('\n','')
            #rint(x1)
            #print(x2)
            ##print(y1)
            #print(y2)
            if x1 == x2 or y1 == y2:
                #print("True")
                expand_points(int(x1),int(x2),int(y1),int(y2),point_dict)
        except:
            break
    with open('convert.txt', 'w') as convert_file: 
     convert_file.write(json.dumps(point_dict))

    count = 0
    for c,v in point_dict.items():
        #print("Coord " + str(c) + " has value " + str(v))
        if v > 1:
            count = count + 1
    return count

print(load_points_hv())