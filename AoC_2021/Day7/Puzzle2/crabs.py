from math import ceil
from statistics import mean

def get_h_pos():
    h_pos_file = open("input.txt")
    h_pos = []
    for h in next(h_pos_file).split(","):
        h_pos.append(int(h))
    return h_pos

def align_crabs():
    h_pos = get_h_pos()
    avg = ceil(mean(h_pos))
    combine_point = 0
    best_h = 0
    best_fuel = 100000000000
    bigH = max(h_pos)
    littleH = min(h_pos)
    print(bigH)
    while combine_point <= bigH:
        fuel = 0
        for h in h_pos:
            steps = abs(h - combine_point)
            cost = (steps*(steps+1))/2
            fuel = int(fuel + cost)
        if fuel < best_fuel:
            best_fuel = fuel
            best_h = combine_point

        combine_point = combine_point + 1
    print(fuel)
align_crabs()
