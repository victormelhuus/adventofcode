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

print(len(instructions))
c = 0
key = "AAA"

while key != "ZZZ":
    for i in instructions:
        print(key, chart[key], i)
        key = step(key, i)
        c +=1 
        if key == "ZZZ": break
    if key == "ZZZ": break

print(c)





