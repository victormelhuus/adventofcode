hands = [{'cards':line.split(" ")[0], 'bet':int(line.split(" ")[1])} for line in open("7des_test.txt").read().split("\n")]
cardvalue = ['x', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

temp = []
for hand in hands:
    likes = {}
    for c in hand['cards']:
        if c not in list(likes.keys()):likes[c] = 1
        else: likes[c] += 1
    num = [likes[t] for t in list(likes.keys())]
    out = hand
    out['num'] = num
    temp.append(out)

hands = temp

def catHand(hand):
    num = hand['num']
    if 5 in num: return "fiveOfKind"
    elif 4 in num: return "fourOfKind"
    elif 3 in num and 2 in num: return "fullHouse"
    elif 3 in num: return "threeOfKind"
    elif num.count(2) == 2: return "twoPairs"
    elif 2 in num: return "pair"
    else: return "highCard"

handByCat = {}
for hand in hands:
    key = catHand(hand)
    if key in list(handByCat.keys()): handByCat[key].append(hand)
    else: handByCat[key] = [hand]

for key in list(handByCat.keys()): print(key, handByCat[key])




