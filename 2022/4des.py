data = open("4des_data.txt").read().split("\n")

pairs= []
for line in data:
    pair = [int(a) for p in line.split(",") for a in p.split("-")]
    pairs.append({'a':pair[0],'b':pair[1],'c':pair[2],'d':pair[3]})

overlaps = [pair for pair in pairs if (pair['a'] <= pair['c'] and pair['b'] >= pair['d']) or (pair['a'] >= pair['c'] and pair['b'] <= pair['d'])]

overlaps2 = [pair
    for pair in pairs
    if (pair['a'])
]

print(len(overlaps))

    