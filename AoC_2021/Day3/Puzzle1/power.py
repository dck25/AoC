bin = open("binary.txt")
result = 0
l = 0
pos = 0

word = next(bin)

p = [0] * (len(word))
p2 = [0] * (len(word))

while l < 1000:
    try:
        for r in word:
            if r == "1":
                p[pos] = p[pos] + 1
            else:
                p2[pos] = p2[pos] + 1
            pos = pos + 1
        l = l + 1
        word = next(bin)
        pos = 0
    except:
        break

gbit = ""
ebit = ""
a = 0
while a < pos:
    if p[a] < p2[a]:
        gbit = gbit + "1"
        ebit = ebit + "0"        
    else:
        gbit = gbit + "0"
        ebit = ebit + "1"  
    a = a + 1
     
print(int(gbit,2)*int(ebit,2))
