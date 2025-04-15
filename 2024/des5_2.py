data = open("des5_data.txt").read().split("\n")
rules = [(int(d.split("|")[0]),int(d.split("|")[1])) for d in data if d.count("|") == 1]
updates = [[int(s) for s in d.split(",")] for d in data if d.count(",")]

def legal(rules, update):
    for rule in rules:
        first, second = rule[0], rule[1]
        if not update.count(first) or not update.count(second): pass #it doesn't contain both numbers
        elif update.index(first) > update.index(second): return False
    return True

bad = [update for update in updates if not legal(rules, update)]

def violations(rules, update):
    viols = []
    for rule in rules:
        first, second = rule[0], rule[1]
        if not update.count(first) or not update.count(second): pass #it doesn't contain both numbers
        elif update.index(first) > update.index(second): viols.append(rule)
    return (update, viols)

def fix(update, rules):
    update, broken_rules = violations(rules, update)
    while True:
        for rule in broken_rules:
            first, second = rule[0], rule[1]
            if update.index(first) > update.index(second):
                update[update.index(first)], update[update.index(second)] = update[update.index(second)], update[update.index(first)]
        if legal(rules, update): break
        else: update, broken_rules = violations(rules, update)
    return update

print(sum([rep[int((len(rep)-1)/2)] for rep in [fix(update,rules) for update in bad]]))

