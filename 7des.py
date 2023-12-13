from operator import itemgetter
hands = [{'cards':line.split(" ")[0], 'bet':int(line.split(" ")[1])} for line in open("7des_test.txt").read().split("\n")]

cardvalue = ["x", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q","K", "A"]


def sortCards(cards):
    temp = sorted([{'card':c, 'v': cardvalue.index(c)} for c in cards], key=itemgetter('v'), reverse=True)
    return "".join([c['card'] for c in temp])

def isBetter(hand1, hand2):
    hand1el, hand2el = {}, {}
    for c in hand1:
        if c not in list(hand1el.keys()):hand1el[c] = 1
        else: hand1el[c] += 1
    for c in hand2:
        if c not in list(hand2el.keys()):hand2el[c] = 1
        else: hand2el[c] += 1
    num1 = [hand1el[key] for key in list(hand1el.keys())]
    num2 = [hand2el[key] for key in list(hand2el.keys())]
    
    #check for alike
    
    
        
    

    
print(isBetter("KK776", "AQQQJ"))

# for hand in hands:
#     print(sortCards(hand['cards']))



def calculateScore(input):
    elements = {}
    for c in input:
        if c not in list(elements.keys()):elements[c] = 1
        else: elements[c] += 1
    score = 0
    keys = list(elements.keys())
    score = 0

    num = [elements[key] for key in keys]
    pairs, threes, singles, fours, fives = [],[],[],[],[]

    for key in keys:
        match elements[key]:
            case 1: singles.append(key)
            case 2: pairs.append(key)
            case 3: threes.append(key)
            case 4: fours.append(key)
            case 5: fives.append(key)
    
    if len(fives):
        score += 100000*cardvalue.index(fives[0])
    elif len(fours):
        score += 10000*cardvalue.index(fours[0])
    
    if len(singles):
        for card in singles:
            score += cardvalue.index(card)
    
    for card in threes: score += 1000*cardvalue.index(card)

    for card in pairs: score += 100*cardvalue.index(card)

    # if 4 in num: #Fire like
    #     score += 10000*(cardvalue.index(elements[keys[num.index(4)]])+1)
    # elif 2 in num and 3 in num: #Fullt hus
    #     score += 1000**(cardvalue.index(elements[keys[num.index(3)]])+1) + 100**(cardvalue.index(elements[keys[num.index(2)]])+1)
    # else:
    #     for key in list(elements.keys()):
    #         score += (cardvalue.index(key)*10 + 1)*10**(elements[key])

    # match len(keys):
    #     case 1: score += elements[keys[0]]*10**5
    #     case 2: 
    #         if [elements[key] for key in keys] == [4, 1]: score += elements[]
 
    # for key in list(elements.keys()):
    #     score += (cardvalue.index(key)*10 + 1)*10**(elements[key])
        # match elements[key]:
    #     #     case 1: score += cardvalue.index(key) + 1
    #     #     case 2: score += 100*(cardvalue.index(key)+1)
    #     #     case 3: score += 1000*(cardvalue.index(key)+1)
    #     #     case 4: score += 10000*(cardvalue.index(key)+1)
    #     #     case 5: score += 100000*(cardvalue.index(key)+1)
    #     # if elements[key] > 1: 
    #     #     score += 1000*(elements[key])*(cardvalue.index(key)+1) + (cardvalue.index(key) + 1)*10
    #     # else: score += cardvalue.index(key) + 1
    return score

# handsScore = sorted([{'cards': hand["cards"], 'bet': hand['bet'], 'score':calculateScore(hand["cards"])} for hand in hands], key=itemgetter("score"))



# [print(hand) for hand in handsScore]

# print(sum([(c+1)*handsScore[c]['bet'] for c in range(len(handsScore))]))