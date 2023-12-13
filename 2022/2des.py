data = open("2des_data.txt").read().split("\n")

code = {'A':'R', 'B':'P', 'C':'S','X':'R', 'Y':'P', 'Z':'S'}
shape_score = {'R':1, 'P':2, 'S':3}
outcome_score = {'L':0, 'D':3, 'W':6}

def game(me, op):
    if me == op: return 'D'
    elif me == 'R' and op == 'P': return 'L'
    elif me == 'R' and op == 'S': return 'W'
    elif me == 'P' and op == 'R': return 'W'
    elif me == 'P' and op == 'S': return 'L'
    elif me == 'S' and op == 'R': return 'L'
    elif me == 'S' and op == 'P': return 'W'

score = 0
for line in data:
    me, op = line.split(" ")[1], line.split(" ")[0]
    res = game(code[me], code[op])
    score += shape_score[code[me]] + outcome_score[res]
    print("me:",code[me],"op:",code[op],"res:",res,"shape:",shape_score[code[me]],outcome_score[res])
print(score)