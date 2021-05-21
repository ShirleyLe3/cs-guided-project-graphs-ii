# _____________________________________________________________________________________________________________________
"""
_______________________________________________________________________________________________________

_______________________________________________________________________________________________________
                    Tool/Method                         KeyWords                
______________________________________________________________________________________________________
Representation
        Linear
                Queue           sorted, shortest, priority
                Stack           track vertices, 

        NonLinear
                Graph                                                                   Direction   Acycl
                                                                                        Direction   Cyclic                  
                                                                                        Undirected  Acyclic 
                                                                                        Undirected  Cyclic 
                    List        dict,  set,  union, intersect, symmetry, difference, no duplicate

                    Matrix      multiple changes/neighbor


DataStructure
                    Linked
                    Tree
                    Graph

Iteration
        Search               single output,          
                    
        Traverse             all paths/nodes, graph, 

        Depth           S    schedule, mapRoutes, match, network analys, 1solution           stack/ list
                        T    graph                                                           adjacency list

        Breadth         S    sorted, shortest, pathing, winning, target, 1shortest           queue
                        T                                                                    matrix



------------------------------------------------------------------------------------------------------

"""


# [ ]DepthFirst Search
"""
DFS(graph):
    for v of graph.verts:
        v.color = white			# marks all verts white
        v.parent = null			# parent/neighbor null

    for v of graph.verts:		# LOOP if unvisited
        if v.color == white:		
            DFS_visit(v)			# pass vert into fn(visit)
	
DFS_visit(v):
    v.color = gray				# mark grey when explored

    for neighbor of v.adjacent_nodes:	#LOOP neighbors unvisited
        if neighbor.color == white:
            neighbor.parent = v		# move up to parnt
            DFS_visit(neighbor)		# loop through other unvisited edges until no white neighbors

    v.color = black					# vert set to black

"""

# [  ]BreadthFirst Search
"""
BFS(graph, startVert):
    for v of graph.vertexes:                    # start with graph & vertex
        v.color = white                         # mark white/visited

    startVert.color = gray                      # currNode = grey (peek, not visit)
        queue.enqueue(startVert)                # add currNode to queueu/list

    while !queue.isEmpty():                     # if queue not empty
        u = queue[0]                            # peek at head of the queue/store, but do not dequeue!

        for v of u.neighbors:                   # LOOP through vert neighbors
            if v.color == white:                # check if unvisited
                v.color = gray                  #          mark gray/peek--> view neighbors
                queue.enqueue(v)                # add vert

        queue.dequeue()                         # remove currNode 
        u.color = black                         # mark black= visited
                                                # continue loop if not empty

"""
# [ ]BreadthFirst Traversal
"""
class Graph:		                        # directed graph. Adjacency list
    def __init__(self):
        self.graph = defaultdict(list)          # default dict to store graph
 
 
    def addEdge(self,u,v):		        # fn to add edge to graph
        self.graph[u].append(v)
 
    def BFS(self, s):			        # print a BFS of graph
        visited = [False] * (max(self.graph) + 1)  # set all vertices not visited
 
        queue = []				# create queue lists       
        queue.append(s)			        # enqueue
        visited[s] = True		        # mark as visited 
 
        while queue:
            s = queue.pop(0)		        # Dequeue a vertex from queue
            print (s, end = " ")
 
            for i in self.graph[s]:	        # Get all adjacent vertices dequeue vertex s
                if visited[i] == False:	        # neighbor not visited
                    queue.append(i)	        # add to queue
                    visited[i] = True  	        # then mark visited 
 
# Create a graph 
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

"""


# [ ]DepthFirst Traversal
"""
class Graph:
 
    def __init__(self):
        self.graph = defaultdict(list)		# default dictionary to store graph
 
    def addEdge(self, u, v):			# add an edge to graph
        self.graph[u].append(v)
 
    def DFSUtil(self, v, visited):
        visited.add(v)	 			# Mark the currode visited
        print(v, end=' ')
 
 
        for neighbour in self.graph[v]:  # Recur for all the adjacent vertices
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
    def DFS(self, v):	 			# DFS traversal & recursion
 
        visited = set()				#  create set to store visited  
        self.DFSUtil(v, visited)		# recursive helper function print traversal
 
 
 
 
# Create a graph given
 
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

"""

"""__________________________________________________________________________________________________
                        UNDERSTAND:
__________________________________________________________________________________________________

______Problem______
- WHAT | parameters? `print(function(testInputs)) `
- HOW | function | action | linear/graph/order
- WHERE| constraints (for:) (while)
- WHEN | constraints (if/else)
- WHY | are variables unique
- WHAT | edge cases



Keywords:





_____Chart/Graph/Map______
DataStruct/Dimension
Vertex =                          (unique)
Edge =                      .     (connection/flow)


________Tool/Method________
- Representation
  - [-] Flow (linear | graph)
  - [-] Direction (uni-direction | bidirectional)
  - [-] Cycle (acyclical | cyclical)
  - [x] List
  - [x] Matrix
- Data Structure
  - [x] Binary
  - [x] LinkedList
  - [x] Stack
  - [x] Queue
- Iteration
  - [x] Traverse | Search
  - [x] Depth | Breadth (sorted)


______Structure Code________
Build Graph
- [Step1]
  - .
  - .
  - .

Iterate & update
- [Step1]
  - .
  - .
  - .
- [Step2]
  - .
  - .
  - .
  - .
    - .
      - .
  - .
  - .
  - .
- [Step3]




__________________________________________________________________________________________________
                        PSUEDO CODE:
__________________________________________________________________________________________________
______Structure________
Build Graph
- [Step1]
  - .
  - .
  - .

Iterate & update
- [Step1]
  - .
  - .
  - .
- [Step2]
  - .
  - .
  - .
  - .
    - .
      - .
  - .
  - .
  - .
- [Step3]

"""
