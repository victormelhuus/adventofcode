import numpy as np
data = open("6des_data.txt").read().split("\n")
pol = np.poly1d([-1, int(str().join([t for t in data[0].split(": ")[1].split(" ") if t.isdigit()])), -int(str().join([d for d in data[1].split(": ")[1].split(" ") if d.isdigit()]))])
print(int(pol.r[0])-int(pol.r[1]))