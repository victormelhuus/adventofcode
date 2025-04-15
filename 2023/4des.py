data = open("4des_data.txt").read().split("\n")

cards = {}
for line in data:
    numbers, winning = [], []
    for num in line.split(":")[1].split("|")[0].split(" "):
        if num.isdigit(): winning.append(num)
    
    for num in line.split(":")[1].split("|")[1].split(" "):
        if num.isdigit(): numbers.append(num)
    cards[line.split(":")[0]] = {"numbers": numbers,"winning": winning}

sum = 0
for card in list(cards.keys()):
    winning_numbers = []
    for num in cards[card]["numbers"]:
        if num in cards[card]["winning"]:
            winning_numbers.append(num)
    
    if len(winning_numbers): 
        sum += 2**(len(winning_numbers)-1)

print(sum)
