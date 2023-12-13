data = open("3des_data.txt").read().split("\n")

priority = "abcdefghijklmnopqrstuvwxyz"
priority += priority.upper()
priority = "-"+priority

sum = 0
for line in data:
    first = line[0:int(len(line)/2)]
    second = line[int(len(line)/2):len(line)]
    overlap = ""
    for c in first:
        if c in second and c not in overlap: overlap += c
    print(overlap)
    for c in overlap: sum += priority.index(c)

print(sum)
