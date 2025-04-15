data = open("des2_data.txt").read().split("\n")

safe = 0
for l in data:
    r = [int(s) for s in l.split(" ")]
    # print(r)
    dir_prev = 0
    unsafe = False
    for i in range(len(r)):
        if i:
            d = r[i-1] - r[i]
            dir = int(d/abs(d)) if d else 0
            if i == 1: dir_prev = dir
            if dir != dir_prev or abs(d) > 3:
                # print("index",i,"prev",r[i-1],"current",r[i])
                # print("UNSAFE",d,dir,dir_prev)
                unsafe = True
                break
            dir_prev = dir
    if not unsafe:
        # print("SAFE") 
        safe += 1

print(safe)          
    