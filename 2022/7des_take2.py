cardvalue = ['x', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
class Hand():
    def __init__(self, cards:str, bet:int):
        self.cards, self.bet, self.likes = cards, bet, {}
        for c in cards:
            if c not in list(self.likes.keys()):self.likes[str(c)] = 1
            else: self.likes[c] += 1
        self.num = [self.likes[t] for t in list(self.likes.keys())]
        self.cat = catHand(self.num)

    def getHighest(self, ignore=[]):
        tuplikes = sorted([(self.likes[key], cardvalue.index(key), key) for key in list(self.likes.keys()) if key not in ignore], reverse=True)
        if not len(tuplikes): return (1, cardvalue.index(self.cards[0]), self.cards[0])
        else: return tuplikes[0]


def isBetter(tup1, tup2):
    if "equal" in [tup1, tup2]: return "equal"
    if tup1[0] == tup2[0]:
        if tup1[1] == tup2[1]: return "tie"
        elif tup1[1] > tup2[1]: return "yes"
        else: return "no"
    elif tup1[0] > tup2[0]: return "yes"
    else: return "no"
    
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
            c = 0
            ignore = []
            while True:
                check = handsSorted[c]
                res = isBetter(hand.getHighest(ignore=ignore), check.getHighest(ignore=ignore))
                if res == 'yes':
                    if c == len(handsSorted)-1:
                        print(res,"End of list, adding ", hand.cards, hand.getHighest(ignore=ignore), check.getHighest(ignore=ignore))
                        handsSorted.append(hand)
                        break
                    ignore = []
                    c+=1
                elif res == "equal":
                    handsSorted.insert(c, hand)
                    break
                elif res == 'no':
                    print("Inserting",hand.cards,"before",check.cards)
                    if c>0:
                        handsSorted.insert(c, hand)
                    else: handsSorted.insert(0, hand)
                    break
                else:
                    ignore.append(hand.getHighest(ignore=ignore)[2])
        else:
            print("Empty list, adding ",hand.cards) 
            handsSorted.append(hand)
    print([hand.cards for hand in handsSorted])
    return handsSorted

hands = [Hand(line.split(" ")[0], int(line.split(" ")[1])) for line in open("7des_test.txt").read().split("\n")]

catHands = {}
for hand in hands:
    if hand.cat not in list(catHands.keys()): catHands[hand.cat] = [hand]
    else: catHands[hand.cat].append(hand)

#[print(key, [hand.cards for hand in catHands[key]]) for key in list(catHands.keys())]

catHandsSorted = {}
for key in catHands: 
    catHandsSorted[key] = sortHands(catHands[key])
    #print(key, [hand.cards for hand in catHandsSorted[key]])


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

