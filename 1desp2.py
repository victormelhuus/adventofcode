data = open('1des_data.txt').read().split('\n')

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine','1','2','3','4','5','6','7','8','9']

def getValue(input):
    if input.isdigit(): return input
    else: return str(numbers.index(input)+1)

sum = 0
for line in data:
    txt = []
    for k in range(len(line)): 
        for num in numbers: 
            i = line.find(num,k)
            if i>-1: txt.append({'value':num, 'index':i+k})
    txt = sorted(txt, key=lambda x:x['index'])
    sum += int(getValue(txt[0]['value']) + getValue(txt[-1]['value']))

print(sum)