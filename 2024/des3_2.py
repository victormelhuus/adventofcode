from re import finditer

data = open("des3_data.txt").read()

dos, donts = [m.end() for m in finditer('do[(][)]', data)], [m.end() for m in finditer("don\'t[(][)]", data)]
muls_first = [m.end() for m in finditer('mul[(]', data)]

muls = []
do = True
for mul in muls_first:
    if do: #Do the thing
        if donts:
            if mul < donts[0]:
                muls.append(mul)
            else:
                donts.pop(0)
                do = False
        else: muls.append(mul)
        if dos:
            if mul > dos[0]: dos.pop(0) #if we have more dos
    else: #Don't do the thing
        if dos:
            if mul > dos[0]:
                muls.append(mul)
                dos.pop(0)
                do = True
            if donts:
                if mul > donts[0]: donts.pop(0) #if we have more donts
        else: break
        

print(muls)

sum = 0
for mul in muls:
    s, i = "", 0
    for c in data[mul:]:
        if c.isnumeric(): s += c
        else: break
        i += 1
    first = int(s)

    s, second = "", None
    if data[mul+i] == ",":
        for c in data[mul+i+1:]:
            if c.isnumeric(): s += c
            elif c == ")": 
                second = int(s)
                break
            else: break
    if second: sum += first * second

print(sum)