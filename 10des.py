data = open("10des_data.txt").read().split("\n")
from collections import deque

parts = {
    '.': [],
    'S': [],
    '|': ['n', 's'],
    '-': ['w', 'e'],
    'L': ['n', 'e'],
    'J': ['n', 'w'],
    '7': ['s', 'w'],
    'F': ['s', 'e']
}

h_max = len(data)
w_max = len(data[0])
class Node():
    def __init__(self, pos, parent, index, distance = None):
        self.pos = pos
        self.parent = parent
        self.index = index
        self.distance = distance
        self.symbol = data[pos[0]][pos[1]]
        self.cons = []
        self.cons_index = []
        self.findConnections()
    
    def findConnections(self):
        if self.pos[0] > 0: 
            n = data[self.pos[0]-1][self.pos[1]]
            if 's' in parts[n]: self.cons.append((self.pos[0]-1, self.pos[1]))
        if self.pos[0] < h_max-1:
            s = data[self.pos[0]+1][self.pos[1]]
            if 'n' in parts[s]: self.cons.append((self.pos[0]+1, self.pos[1]))
        if self.pos[1] < w_max-1:
            e = data[self.pos[0]][self.pos[1]+1]
            if 'w' in parts[e]: self.cons.append((self.pos[0], self.pos[1]+1))
        if self.pos[1] > 0:
            w = data[self.pos[0]][self.pos[1]-1]
            if 'e' in parts[w]: self.cons.append((self.pos[0], self.pos[1]-1))
        #print('n:',n,'s:',s,'e:',e,'w:',w)
        
start = [(i,data[i].index("S")) for i in range(len(data)) if "S" in data[i]][0]
tree = [Node(start, None, 0)]
added = [start]
i = 0

#Construct tree
print("Constructing tree")
while i < len(tree):
    currnode = tree[i]
    l = len(tree)
    for con in currnode.cons:
        if con not in added:
            added.append(con) 
            tree.append(Node(con, i, l))
            tree[i].cons_index.append(l)
            l += 1

    if i >= len(tree): break
    i += 1

print("Collecting edges")
edges = []
for n in tree:
    for i in n.cons_index:
        v = (n.index, i)
        if v not in edges: edges.append(v)

from collections import deque
class Graph:
    # Initialisation of graph
    def __init__(self, vertices):
 
        # No. of vertices
        self.vertices = vertices
 
        # adjacency list
        self.adj = {i: [] for i in range(self.vertices)}
 
    def addEdge(self, u, v):
        # add u to v's list
        self.adj[u].append(v)
        # since the graph is undirected
        self.adj[v].append(u)
 
    # method return farthest node and its distance from node u
    def BFS(self, u):
        # marking all nodes as unvisited
        visited = [False for i in range(self.vertices + 1)]
        # mark all distance with -1
        distance = [-1 for i in range(self.vertices + 1)]
 
        # distance of u from u will be 0
        distance[u] = 0
        # in-built library for queue which performs fast operations on both the ends
        queue = deque()
        queue.append(u)
        # mark node u as visited
        visited[u] = True
 
        while queue:
 
            # pop the front of the queue(0th element)
            front = queue.popleft()
            # loop for all adjacent nodes of node front
 
            for i in self.adj[front]:
                if not visited[i]:
                    # mark the ith node as visited
                    visited[i] = True
                    # make distance of i , one more than distance of front
                    distance[i] = distance[front]+1
                    # Push node into the stack only if it is not visited already
                    queue.append(i)
 
        maxDis = 0
 
        # get farthest node distance and its index
        for i in range(self.vertices):
            if distance[i] > maxDis:
 
                maxDis = distance[i]
                nodeIdx = i
 
        return nodeIdx, maxDis
 
    # method prints longest path of given tree
    def LongestPathLength(self):
 
        # first DFS to find one end point of longest path
        node, Dis = self.BFS(0)
 
        # second DFS to find the actual longest path
        node_2, LongDis = self.BFS(node)
 
        print('Longest path is from', node, 'to', node_2, 'of length', LongDis)

print("Finding longest path")
G = Graph(len(edges)+1)
for edge in edges: G.addEdge(*edge)
G.LongestPathLength()





