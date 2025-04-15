f = open('2des_data.txt', 'r')
data = f.read().split('\n')
f.close()

bagOfCubes = {"red": 12,"green": 13,"blue": 14}
games = {}
for line in data:
    rounds = []
    for round in line.split(": ")[1].split("; "):
        temp = {}
        for color in round.split(", "): 
            temp[color.split(" ")[1]] = color.split(" ")[0]
        rounds.append(temp)
    games[line.split(":")[0].split(" ")[1]] = rounds

sum = 0
for game in list(games.keys()):
    possible = True
    for round in games[game]:
        for color in list(round.keys()):
            if int(round[color]) > bagOfCubes[color]:
                possible = False
                break
        if not possible: break
    if possible: sum += int(game)

print(sum)




