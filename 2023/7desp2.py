cardvalue = ['x','J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
class Hand():
    def __init__(self, cards:str, bet:int):
        self.cards, self.bet = cards, bet
        self.likes = self.cardLikes()
        self.num = [self.likes[t] for t in list(self.likes.keys())]
        self.cat = catHand(self.num)

    def cardLikes(self):
        likes = {}
        for c in self.cards:
            if c not in list(likes.keys()):likes[str(c)] = 1
            else: likes[c] += 1
        keys = list(likes.keys())
        if "J" in keys:
            num = [likes[t] for t in keys]
            if 5 not in num:
                num[keys.index("J")] = 0
                for _ in range(likes['J']): 
                    if 4 in num: #We can upgrade to fiveOK
                        select = keys[num.index(4)]
                        if select != "J": 
                            likes[select] += 1
                            likes["J"] -= 1
                    elif 3 in num: #We can ugrade to a fourOK
                        select = keys[num.index(3)]
                        if select != "J": 
                            likes[select] += 1 
                            likes["J"] -= 1
                    elif num.count(2) == 2: #We can upgrade to full house
                        indexes = [i for i, x in enumerate(num) if x==2]
                        select = keys[indexes[0]]
                        if select == "J": select == keys[indexes[1]]
                        likes[select] += 1 
                        likes["J"] -= 1
                    elif 2 in num: #Upgrade to threeOK
                        select = keys[num.index(2)]
                        if select != "J": 
                            likes[select] += 1
                            likes["J"] -= 1
                    else: #Upgrade to pair
                        indexes = [i for i, x in enumerate(num) if x==1]
                        select = keys[indexes[0]]
                        k = 1
                        while select == "j": 
                            select = keys[indexes[0]]
                            k += 1
                        likes[select] += 1
                        likes["J"] -= 1
                    num = [likes[t] for t in keys]
                    num[keys.index("J")] = 0
        return likes


def catHand(num):
    if 5 in num: return "fiveOK"
    elif 4 in num: return "fourOK"
    elif 3 in num and 2 in num: return "house"
    elif 3 in num: return "threeOK"
    elif num.count(2) == 2: return "twoPairs"
    elif 2 in num: return "pair"
    else: return "HC"


def sortHands(myhands):
    handsSorted = []
    for hand in myhands:
        if len(handsSorted):
            h, c = 0, 0
            while True:
                check = handsSorted[h]
                if cardvalue.index(hand.cards[c]) > cardvalue.index(check.cards[c]):
                    if h == len(handsSorted)-1:
                        handsSorted.append(hand)
                        break
                    c = 0
                    h += 1
                elif cardvalue.index(hand.cards[c]) == cardvalue.index(check.cards[c]):
                    if c < 5: c += 1
                    else:
                        handsSorted.insert(h, hand)
                        break
                else:
                    if h>0: handsSorted.insert(h, hand)
                    else: handsSorted.insert(0, hand)
                    break
        else: handsSorted.append(hand)
    return handsSorted

hands = [Hand(line.split(" ")[0], int(line.split(" ")[1])) for line in open("7des_data.txt").read().split("\n")]

catHands = {}
for hand in hands:
    if hand.cat not in list(catHands.keys()): catHands[hand.cat] = [hand]
    else: catHands[hand.cat].append(hand)

catHandsSorted = {}
for key in catHands: catHandsSorted[key] = sortHands(catHands[key])

sortedHands = []
if "HC" in list(catHandsSorted.keys()): sortedHands.extend(catHandsSorted['HC'])
if "pair" in list(catHandsSorted.keys()): sortedHands.extend(catHandsSorted['pair'])
if "twoPairs" in list(catHandsSorted.keys()): sortedHands.extend(catHandsSorted['twoPairs'])
if "threeOK" in list(catHandsSorted.keys()): sortedHands.extend(catHandsSorted['threeOK'])
if "house" in list(catHandsSorted.keys()): sortedHands.extend(catHandsSorted['house'])
if "fourOK" in list(catHandsSorted.keys()): sortedHands.extend(catHandsSorted['fourOK'])
if "fiveOK" in list(catHandsSorted.keys()): sortedHands.extend(catHandsSorted['fiveOK'])

[print(c+1, sortedHands[c].cards, sortedHands[c].bet, sortedHands[c].cat) for c in range(len(sortedHands))]

print(sum([(c+1)*sortedHands[c].bet for c in range(len(sortedHands))]))

