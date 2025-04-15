data = open("des6_test.txt").read().split("\n")
pos = [(r, data[r].index("^")) for r in range(len(data)) if data[r].count("^")][0]

class Guard:
    def __init__(self, pos, map):
        self.pos = pos
        self.visits = 1
        self.direction = "up"
        self.map = [list(l) for l in map]
        self.map[self.pos[0]][self.pos[1]] = "X"
        self.path = []
        self.new_path = []

    def mark(self):
        r, c = self.pos
        if self.map[r][c] != "X": 
            self.map[r][c] = "X"
            self.visits += 1
    
    def move(self):
        r, c = self.pos
        match self.direction:
            case "up":
                if r-1 < 0: return False
                if self.map[r-1][c] == "#": self.direction = "right"
                else: r -= 1
            case "right":
                if c+1 >= len(self.map[0]): return False
                if self.map[r][c+1] == "#": self.direction = "down"
                else: c += 1
            case "down":
                if r+1 >= len(self.map): return False
                if self.map[r+1][c] == "#": self.direction = "left"
                else: r += 1
            case "left":
                if c-1 < 0 : return False
                if self.map[r][c-1] == "#": self.direction = "up"
                else: c -= 1
        if r < 0 or c < 0: return False
        self.pos = (r, c)
        self.mark()
        return True
    
    def discover(self):
        con = True
        while con:
            try: con = self.move()
            except IndexError: break
            except Exception as e: print(e)
            if con:
                if self.path:
                    if self.path[-1][0] != self.pos: self.path.append((self.pos, self.direction))
                    else: self.path[-1] = (self.pos, self.direction)
                else: self.path.append((self.pos, self.direction))
        return self.visits
    
    def isItLoop(self):
        while True:
            if not self.move(): return False
            if (self.pos, self.direction) in self.new_path: return True
            self.new_path.append((self.pos, self.direction))

    def placeAndCheck(self):
        self.discover()
        places = []
        backtrack = self.path
        print(self.path)
        for i in range(len(self.path)):
            print(i, len(backtrack))
            if len(backtrack) -i < 2: break
            self.pos, self.direction = backtrack[-i-2]
            pos, dir = backtrack[-i-1]
            r, c = pos
            self.map[r][c] = "#"
            self.new_path = backtrack[:len(backtrack)-i-3]
            if self.isItLoop(): 
                places.append((r,c))
                self.map[r][c] = "O"
                print("here")
                #[print("".join(l)) for l in self.map]
            self.map[r][c] = "."

        return places
            


guard = Guard(pos, data)

print("-------part - 1-------")
v=guard.discover()
[print("".join(l)) for l in guard.map]
print(v)

print("-------part - 2-------")
print(len(guard.placeAndCheck()))