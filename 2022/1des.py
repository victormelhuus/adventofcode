data = open("1des_data.txt").read().split("\n")

calories = {}
c = 0
for line in data:
    if line != "":
        if str(c) not in list(calories.keys()): calories[str(c)] = [int(line)]
        else: calories[str(c)].append(int(line))
    else: c +=1

elfs = []
for elf in list(calories.keys()): elfs.append(sum(calories[elf]))

print("Part 1:", max(elfs))
print("Part 2:", sum(sorted(elfs, reverse=True)[0:3]))

