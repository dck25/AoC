def get_fishes():
    fish_file = open("fish.txt")
    fishes = next(fish_file).split(",")
    fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for fish in fishes:
        fish_dict[int(fish)] = fish_dict[int(fish)] + 1

    fish_file.close()
    return fish_dict

def spawn_fish(days):
    fish_dict = get_fishes()
    
    while days > 0:
        i = 0
        s = 0
        if i == 0:
            s = fish_dict[0]
            fish_dict[0] = 0
            i = 1
        while i <= 8:
            if i == 7:
                fish_dict[6] = fish_dict[7] + s
            else:
                fish_dict[int(i)-1] = fish_dict[int(i)]
            i = i + 1
        fish_dict[8] = s
        days = days - 1
    sum = 0
    for f,v in fish_dict.items():
        sum = sum + v

    print(sum)


spawn_fish(256)
