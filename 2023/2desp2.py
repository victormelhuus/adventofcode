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
    min = {'red':None, 'green':None, 'blue':None}
    for color in list(min.keys()):
        for round in games[game]:
            if color in round.keys():
                if min[color] == None or int(round[color]) > min[color]:
                    min[color] = int(round[color])
    sum += min['red']*min['green']*min['blue']

print(sum)

