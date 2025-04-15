data = open("des2_data.txt").read().split("\n")

safe = 0
for l in data:
    #print("-------------------")
    r = [int(s) for s in l.split(" ")]
    # print(r)
    dir_prev = 0
    unsafe = False
    removed = False
    beacuse = ""
    for i in range(len(r)):
        if i:
            d = r[i-1] - r[i]
            dir = int(d/abs(d)) if d else 0
            if i == 1: dir_prev = dir
            if dir != dir_prev or abs(d) > 3: #part 1 unsafe
                #print("Unsafe first part",r[i], dir,"!=", dir_prev,"or", abs(d),">",3)
                # unsafe  = True
                # break
                #Part 2 unsafe
                if i == len(r)-1: #if we're at the last element. Removing it makes it safe
                    unsafe = False
                    break
                d2 = r[i-1] - r[i+1]
                dir2 = int(d2/abs(d2)) if d2 else 0
                if dir2 != dir_prev or abs(d2) > 3 or removed:
                    if i == 1: #Check if removing the first element makes it safe
                        d3 = r[i] - r[i+1]
                        dir3 = int(d3/abs(d3)) if d3 else 0
                        if dir2 != dir_prev or abs(d2) > 3 or removed:
                            unsafe = True
                            beacuse = " (first element) " + str(r[i]) + " " + str(dir2) + " != " + str(dir_prev) + " or " + str(abs(d2)) + " > 3 or " + str(removed)
                            break
                        else:
                            removed = True
                            dir_prev = dir3
                            #print("safe with remove",r[i], dir3, dir_prev, abs(d3))
                    else:
                        beacuse = " (stage 2) " + str(r[i]) + " " + str(dir2) + " != " + str(dir_prev) + " or " + str(abs(d2)) + " > 3 or " + str(removed)
                        unsafe = True
                        break
                else:
                    removed = True
                    dir_prev = dir2
                    #print("safe with remove",r[i], dir2, dir_prev, abs(d2))
            else:   
                dir_prev = dir
    if not unsafe:
        #print(r,"SAFE") 
        safe += 1
    else:
        print(r,"UNSAFE BECAUSE",beacuse)

print(safe)          
    