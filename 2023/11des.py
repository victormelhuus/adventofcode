data = open("2023/11des_data.txt").read().split("\n")
from math import sqrt
expansion = 1000000-1

#check for expansion'
print("check for expansion")
rows = [int(l) for l in range(len(data)) if "#" not in data[l]]
cols = [int(c) for c in range(len(data[0])) if "#" not in [data[l][c] for l in range(len(data))]]

print("rows",rows)
print("cols",cols)

#Get line coordinates
print("get line coordinates")
stars = []
l = 0
for line in data:
    c=0
    for char in line:
        if char == "#":
            stars.append((l,c))
        c += 1
    l += 1

#Expand stars
ex_stars = []
for star in stars:
    x1, y1 = star
    x1 += len([row for row in rows if row < x1])*expansion
    y1 += len([col for col in cols if col < y1])*expansion
    ex_stars.append((x1, y1))
    
#Get all possible lines
print("get all possible lines")
lines = []
for i in range(len(ex_stars)):
    for j in range(i+1, len(ex_stars)):
        x1, y1 = ex_stars[i]
        x2, y2 = ex_stars[j]
        lines.append((x1, y1, x2, y2,))

print(len(lines))

#Calculate all distances
print("calculate all distances")
distances = []
for line in lines:
    x1, y1, x2, y2 = line
    distances.append(abs(x2-x1) + abs(y2-y1))

print(sum(distances))