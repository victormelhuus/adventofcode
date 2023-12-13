import math
data = open("6des_data.txt").read().split("\n")
time = [int(t) for t in data[0].split(": ")[1].split(" ") if t.isdigit()]
distance = [int(d) for d in data[1].split(": ")[1].split(" ") if d.isdigit()]

def race(hold_time, time): return (time-hold_time)*hold_time
print(math.prod([sum([1 for h in range(time[r]) if race(h, time[r]) > distance[r]]) for r in range(len(time))]))
