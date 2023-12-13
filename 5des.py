data = open("5des_data.txt").read().split("\n")

#Exctract data
seeds = data[0].split(": ")[1].split(" ")
data.pop(0)

range_lists, temp, key = {}, [], ""
for line in [*data, ""]:
    if line !="":
        if line[0].isdigit(): temp.append(line.split(" "))
        else: key = line.replace(":","")
    elif len(temp):
        range_lists[key] = [{'dest':int(temp[k][0]), 'src':int(temp[k][1]), 'l':int(temp[k][2])} for k in range(len(temp))]
        temp = []

def seed_path(value:int, keys:list):
    if len(keys):
        key = keys.pop(0)
        for r in range_lists[key]:
            if value >= r['src'] and value <= r['src'] + r['l'] -1:
                value = r['dest'] + value - r['src']
                return seed_path(value, keys)
        return seed_path(value, keys)
    else: return value
    
print(min([seed_path(int(seed), list(range_lists.keys())) for seed in seeds]))