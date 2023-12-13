data = open("4des_data.txt").read().split("\n")

cards = {}

for line in data:
    cards[line.split(":")[0].split(" ")[-1]] = {"numbers": [num for num in line.split(":")[1].split("|")[1].split(" ") if num.isdigit()],"winning": [num for num in line.split(":")[1].split("|")[0].split(" ") if num.isdigit()], 'instances':1}

for card in list(cards.keys()):
    winning_numbers = [num for num in cards[card]["numbers"] if num in cards[card]["winning"]]
    if len(winning_numbers):
        for i in range(len(winning_numbers)):
            cards[str(int(card)+i+1)]["instances"] += cards[card]['instances']

print(sum([cards[card]['instances'] for card in list(cards.keys())]))