data = [block.split("\n") for block in open("2023/13des_test.txt").read().split(" ")]

print(data[0][0][:])

for block in data: 
    #vertical pivot
    for r in range(len(block)-1):
        if block[r] == block[r+1]: #found a pivot
            print("here", block[r], block[r+1])