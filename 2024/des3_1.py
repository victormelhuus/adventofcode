from re import finditer

data = open("des3_data.txt").read()

sum = 0
for mul in [m.end() for m in finditer('mul[(]', data)]:
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

