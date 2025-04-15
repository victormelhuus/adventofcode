data = open("5des_data.txt").read().split("\n")

seeds_raw = data[0].split(": ")[1].split(" ")
myseeds = [{'min':int(seeds_raw[l]), 'max':int(seeds_raw[l]) + int(seeds_raw[l+1])-1} for l in range(0,len(seeds_raw),2)]

data.pop(0) 

range_lists, temp, key = {}, [], ""
for line in [*data, ""]:
    if line !="":
        if line[0].isdigit(): temp.append([int(s) for s in line.split(" ")])
        else: key = line.replace(":","")
    elif len(temp):
        range_lists[key] = [{'destStart':temp[k][0], 'destEnd': temp[k][0] + temp[k][2]-1, 'srcStart':temp[k][1], 'srcEnd':temp[k][1] + temp[k][2]-1} for k in range(len(temp))]
        temp = []

def newSeedSpan(seed, r):
    destMin, destMax, srcMin, srcMax = r['destStart'], r['destEnd'], r['srcStart'], r['srcEnd']
    smin, smax = seed['min'], seed['max']
    if smin < srcMax and smax > srcMin: #Check if in span
        if smax < srcMax: newMax = smax - srcMin + destMin 
        else: newMax = destMax
    
        if smin > srcMin: newMin = smin - srcMin + destMin 
        else: newMin = destMin

        return {'min':newMin, 'max':newMax}
    else: return None

def seed_path(seeds, keys):
    first_run = True
    while True:
        if first_run: 
            first_run = False
            new_seeds, temp_seeds = seeds, []
        else: new_seeds, temp_seeds = temp_seeds, []

        key = keys.pop(0)
        for seed in new_seeds:
            added = False
            for r in range_lists[key]:
                a = newSeedSpan(seed, r)
                if a != None and a not in temp_seeds: #Ignore duplicate seeds
                    added = True
                    temp_seeds.append(a)
            if not added: temp_seeds.append(seed)
        if not len(keys): return temp_seeds 
            
print(min([reg['min'] for reg in seed_path(myseeds, list(range_lists.keys()))]))