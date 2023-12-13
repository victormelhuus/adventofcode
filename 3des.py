f = open('3des_data.txt', 'r')
data = f.read().replace(" ","").split("\n")
f.close()

def is_a_symbol(c):
    return not c.isnumeric() and c != "."

height, width = len(data), len(data[0])
numbers = []
for row in range(height):
    numstr = ""
    start_col = 0
    for col in range(width):
        if data[row][col].isnumeric() and col < width -1:
            numstr += data[row][col]
            if col > 0:
                if not data[row][col-1].isnumeric(): start_col = col
        else: #Gather the data
            if (len(numstr) and data[row][col-1].isnumeric()) or data[row][col].isnumeric():
                if data[row][col].isnumeric():
                    if not data[row][col].isnumeric(): start_col = col 
                    numstr += data[row][col] #If it is the last number on the row

                #Check the surroundings
                surr = []
                if data[row][col].isnumeric() and col == width-1:
                    if row > 0:
                        #if data[row][col] == '9': print("here")
                        surr.append(data[row-1][start_col:col+1]) #Top mid
                        if start_col > 0: surr.append(data[row-1][start_col-1]) #Left top diagonal
                        if col < width -1: surr.append(data[row-1][col+1]) #Right top diagonal
                    if start_col > 0:
                        surr.append(data[row][start_col-1]) #Left
                    if row < height-1:
                        surr.append(data[row+1][start_col:col+1]) #Bottom mid
                        if start_col > 0: surr.append(data[row+1][start_col-1]) #Left top diagonal
                        if col < width -1: surr.append(data[row+1][col+1]) #Right top diagonal
                else:
                    if row > 0:
                        #if data[row][col] == '9': print("here")
                        surr.append(data[row-1][start_col:col]) #Top mid
                        if start_col > 0: surr.append(data[row-1][start_col-1]) #Left top diagonal
                        if col < width -1: surr.append(data[row-1][col]) #Right top diagonal
                    if start_col > 0:
                        surr.append(data[row][start_col-1]) #Left
                    if col < width -1:
                        surr.append(data[row][col]) #Right
                    if row < height-1:
                        surr.append(data[row+1][start_col:col]) #Bottom mid
                        if start_col > 0: surr.append(data[row+1][start_col-1]) #Left bottom diagonal
                        if col <= width -1:
                            surr.append(data[row+1][col]) #Right bottom diagonal

                keep = False
                for s in surr:
                    for c in s:
                        if is_a_symbol(c):
                            keep = True
                            break
                    if keep:
                        numbers.append(int(numstr)) 
                        break
                #print(numstr, surr, keep)
            start_col = 0
            numstr = ""

print(sum(numbers))
print(numbers)