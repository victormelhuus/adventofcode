cardvalue = ['x', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
class Hand():
    def __init__(self, cards:str, bet:int):
        self.cards, self.bet, self.likes = cards, bet, {}
        for c in cards:
            if c not in list(self.likes.keys()):self.likes[str(c)] = 1
            else: self.likes[c] += 1
        self.num = [self.likes[t] for t in list(self.likes.keys())]
        self.cat = catHand(self.num)

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
for key in catHands: 
    catHandsSorted[key] = sortHands(catHands[key])


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

