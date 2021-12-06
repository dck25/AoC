def get_fishes():
    fish_file = open("fish_test.txt")
    fishes = next(fish_file).split(",")
    fish_list = []
    for fish in fishes:
        fish_list.append(int(fish))
    fish_file.close()
    return fish_list

def spawn_fish(days):
    fish_list = get_fishes()
    while days > 0:
        i = len(fish_list) - 1
        while i >= 0:
            if fish_list[i] == 0:
                fish_list[i] = 6
                fish_list.append(8)
            else: fish_list[i] = fish_list[i] - 1
            i = i - 1
        days = days - 1
    print(len(fish_list))

spawn_fish(10)
