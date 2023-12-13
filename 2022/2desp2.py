data = open("2des_data.txt").read().split("\n")

code = {'A':'R', 'B':'P', 'C':'S','X':'L', 'Y':'D', 'Z':'W'}
shape_score = {'R':1, 'P':2, 'S':3}
outcome_score = {'L':0, 'D':3, 'W':6}


def game(res, op):
    if res == 'D': return op
    elif op == 'P' and res == 'L': return 'R' 
    elif op == 'P' and res == 'W': return 'S' 
    elif op == 'S' and res == 'L': return 'P' 
    elif op == 'S' and res == 'W': return 'R' 
    elif op == 'R' and res == 'L': return 'S' 
    elif op == 'R' and res == 'W': return 'P' 

score = 0
for line in data:
    res, op = line.split(" ")[1], line.split(" ")[0]
    me = game(code[res], code[op])
    score += shape_score[me] + outcome_score[code[res]]
    #print("me:",code[me],"op:",code[op],"res:",res,"shape:",shape_score[code[me]],outcome_score[res])
print(score)