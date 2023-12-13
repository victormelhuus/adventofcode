data = [[int(v) for v in line.split(" ")] for line in open("9des_data.txt").read().split("\n")]

def findDiff(mylist): return [mylist[i+1] - mylist[i] for i in range(len(mylist)-1)]
        
def findDiffs(mylist):
    out = [mylist]
    diff = mylist
    while True:
        diff = findDiff(diff)
        if len([v for v in diff if v == 0]) == len(diff): break
        out.append(diff)
    return out

def findNext(mylist):
    for i in range(len(mylist)-1, 0, -1):
        mylist[i-1].append(mylist[i][-1] + mylist[i-1][-1])
    return mylist[0][-1]

withDiffs = [findDiffs(a) for a in data]

s = 0
for i in range(len(withDiffs)): s += findNext(withDiffs[i])

print("part1:",s)

def findPrev(mylist):
    for i in range(len(mylist)-1, 0, -1): 
        mylist[i-1].insert(0,mylist[i-1][0]-mylist[i][0])
    return mylist[0][0]

s = 0
for i in range(len(withDiffs)): s += findPrev(withDiffs[i])

print("part2:",s)
