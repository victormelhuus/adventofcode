from math import lcm
data = open("8des_data.txt").read().split("\n")
instructions = data.pop(0) + data.pop(0)

chart = {}
for line in data:
    key = line.split(" = ")[0]
    v = line.split(" = ")[1].replace("(","").replace(")","").split(", ")
    chart[key] = (v[0], v[1])


def step(curkey, direction):
    if direction == 'L': return chart[curkey][0]
    else: return chart[curkey][1]

keys = [key for key in list(chart.keys()) if key[2] == 'A']

loops = []
for k in keys:
    c = 0
    key = k
    while key[2] != "Z":
        for i in instructions:
            key = step(key, i)
            c +=1 
            if key[2] == "Z": break
        if key[2] == "Z": break
    loops.append(c)

print(*loops)

print(lcm(*loops))

