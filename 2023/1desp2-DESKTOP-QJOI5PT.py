f = open('1des_data.txt', 'r')
data = f.read().split('\n')
f.close()

sum = 0
for word in data:
    ints = [c for c in word if c.isdigit()]
    sum += int(ints[0] + ints[-1])
    
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
