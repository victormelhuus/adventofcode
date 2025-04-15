data= open('1des_data.txt', 'r').read().split("\n")
sum = 0
for line in data:
    ints = [c for c in line if c.isdigit()]
    sum += int(ints[0] + ints[-1])
print(sum)