data = open("3des_data.txt").read().split("\n")

priority = "abcdefghijklmnopqrstuvwxyz"
priority += priority.upper()
priority = "-"+priority

sum = 0
c = 0
for line in data:
    temp = []
    if c < 3: 
        temp.append(line)
    else:
        c = 0


