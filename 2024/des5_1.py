data = open("des5_test.txt").read().split("\n")
rules = [(int(d.split("|")[0]),int(d.split("|")[1])) for d in data if d.count("|") == 1]
updates = [[int(s) for s in d.split(",")] for d in data if d.count(",")]

def legal(rules, update):
    for rule in rules:
        first, second = rule[0], rule[1]
        if not update.count(first) or not update.count(second): pass #it doesn't contain both numbers
        elif update.index(first) > update.index(second): return False
    return True

good = [update for update in updates if legal(rules, update)]
print(sum([g[int((len(g)-1)/2)] for g in good]))
bad = [update for update in updates if not legal(rules, update)]
print(bad)