f = open('3des_test.txt', 'r')
data = f.read().replace(" ","").split("\n")
f.close()

def is_a_symbol(c):
    return not c.isnumeric() and c != "."

def check_for_star(starlist:list, c:str, row, col):
    if c == "*":
        starlist.append((row,col))
    return starlist

def check_for_stars(starlist:list, c:str, row, col_start, col_end):
    i = 0
    for col in range(col_start, col_end):
        if c[i] == "*":
            starlist.append((row,col))
        i +=1
    return starlist

height, width = len(data), len(data[0])
numbers = []
numbers_with_star = []
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
                    #start_col = col 
                    numstr += data[row][col] #If it is the last number on the row
                my_stars = []
                #Check the surroundings
                surr = []
                if data[row][col].isnumeric() and col == width-1:
                    if start_col == 0: start_col = col
                    if row > 0:
                        surr.append(data[row-1][start_col:col+1]) #Top mid
                        my_stars = check_for_stars(my_stars,data[row-1][start_col:col+1],row-1,start_col,col+1)
                        if start_col > 0: 
                            surr.append(data[row-1][start_col-1]) #Left top diagonal
                            my_stars = check_for_star(my_stars, data[row-1][start_col-1],row-1,start_col-1 )
                        if col < width -1:
                            surr.append(data[row-1][col+1]) #Right top diagonal
                            my_stars = check_for_star(my_stars, data[row-1][col+1], row-1, col+1) 
                    if start_col > 0:
                        surr.append(data[row][start_col-1]) #Left
                        my_stars = check_for_star(my_stars,data[row][start_col-1], row, start_col-1)
                    if row < height-1:
                        surr.append(data[row+1][start_col:col+1]) #Bottom mid
                        my_stars = check_for_stars(my_stars, data[row+1][start_col:col+1], row+1,start_col, col+1)
                        if start_col > 0: 
                            surr.append(data[row+1][start_col-1]) #Left top diagonal
                            my_stars = check_for_star(my_stars, data[row+1][start_col-1], row +1, start_col-1)
                        if col < width -1: 
                            surr.append(data[row+1][col+1]) #Right top diagonal
                            my_stars = check_for_star(my_stars,data[row+1][col+1], row+1, col+1)
                        
                else:
                    if row > 0:
                        surr.append(data[row-1][start_col:col]) #Top mid
                        my_stars = check_for_stars(my_stars,data[row-1][start_col:col], row-1, start_col, col)
                        if start_col > 0: 
                            surr.append(data[row-1][start_col-1]) #Left top diagonal
                            my_stars = check_for_star(my_stars, data[row-1][start_col-1], row-1, start_col-1)
                        if col < width -1: 
                            surr.append(data[row-1][col]) #Right top diagonal
                            my_stars = check_for_star(my_stars,data[row-1][col], row-1,col)
                    if start_col > 0:
                        surr.append(data[row][start_col-1]) #Left
                        my_stars = check_for_star(my_stars,data[row][start_col-1], row, start_col-1)
                    if col < width -1:
                        surr.append(data[row][col]) #Right
                        my_stars = check_for_star(my_stars,data[row][col], row, col)
                    if row < height-1:
                        surr.append(data[row+1][start_col:col]) #Bottom mid
                        my_stars = check_for_stars(my_stars, data[row+1][start_col:col], row+1, start_col, col)
                        if start_col > 0: 
                            surr.append(data[row+1][start_col-1]) #Left bottom diagonal
                            my_stars = check_for_star(my_stars,data[row+1][start_col-1], row+1, start_col-1)
                        if col <= width -1:
                            surr.append(data[row+1][col]) #Right bottom diagonal
                            my_stars = check_for_star(my_stars,data[row+1][col], row+1, col)

                if len(my_stars):
                    numbers_with_star.append({"num":numstr, "stars":my_stars[0]})
                keep = False
                for s in surr:
                    for c in s:
                        if is_a_symbol(c):
                            keep = True
                            break
                    if keep:
                        numbers.append(int(numstr)) 
                        break
                
            start_col = 0
            numstr = ""

print('Part 1:',sum(numbers))

stars = {}
for item in numbers_with_star:
    key = str(item["stars"][0]) + str(item["stars"][1])
    if key in list(stars.keys()):
        stars[key].append(item["num"])
    else:
        stars[key] = [item["num"]]

print(stars)

ratios = []
for star in list(stars.keys()):
    if len(stars[star]) == 2:
        ratios.append(int(stars[star][0])*int(stars[star][1]))
        
print("Part 2:",sum(ratios))
