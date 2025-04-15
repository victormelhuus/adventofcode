data = open("des1_data.txt").read().split("\n")

left, right = [int(d.split(" ")[0]) for d in data], [int(d.split(" ")[-1]) for d in data]

#part 1
new_list = []
while len(left):
    mleft, mright = min(left), min(right)
    new_list.append((mleft, mright))
    left.pop(left.index(mleft))
    right.pop(right.index(mright))

print("part 1:",sum([abs(i[0]-i[1]) for i in new_list]))

#part 2
left = [int(d.split(" ")[0]) for d in data]
right = [int(d.split(" ")[-1]) for d in data]

print(sum([nl*right.count(nl) for nl in left]))