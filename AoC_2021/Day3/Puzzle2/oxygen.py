ls = open("binary.txt")

oxygen = [x for x in ls]
carbon = [x for x in oxygen]

i = 0
count = 0
oxy_length = len(oxygen[0])
while len(oxygen) > 1:
    oxygen.sort()
    if oxygen[len(oxygen)//2][i] == "0":
        oxygen = [x for x in oxygen if x[i]=="0"]
    else:
        oxygen = [x for x in oxygen if x[i]=="1"]
    i = i + 1


i = 0
count = 0
carbon_length = len(carbon[0])
while len(carbon) > 1:
    carbon.sort()
    if carbon[len(carbon)//2][i] == "0":
        carbon = [x for x in carbon if x[i]=="1"]
    else:
        carbon = [x for x in carbon if x[i]=="0"]
    i = i + 1


print(int(carbon[0],2)*int(oxygen[0],2))