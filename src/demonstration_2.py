# --------------------------------------------------------------------
#                       Adjacent Matrix
# ____________________________________________________________________

"""
An `image` is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).

Given a coordinate `(sr, sc)` representing the starting pixel (row and column)
of the flood fill, and a pixel value `newColor`, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels (also
with the same color as the starting pixel), and so on. Replace the color of all
of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:

```plaintext
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels
connected by a path of the same color as the starting pixel are colored with
the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.
```

Notes:

- The length of `image` and `image[0]` will be in the range `[1, 50]`.
- The given starting pixel will satisfy `0 <= sr < image.length` and
`0 <= sc < image[0].length`.
- The value of each color in `image[i][j]` and `newColor` will be an integer in
`[0, 65535]`.

    Inputs:
    image -> List[List[int]]
    sr -> int
    sc -> int
    new_color -> int

    Output:
    List[List[int]]
    """


def flood_fill(image, sr, sc, new_color):
    current_color = image[sr][sc]
    # Traverse!
    queue = []
    visited = set()
    queue.append((sr, sc))


​
 while len(queue) > 0:
      # pop the item off the queue
      current_vertex = queue.pop(0)
       # check if vertex was visited
       if current_vertex in visited:
            continue

        visited.add(current_vertex)
        # update the pixel to the new color
        image[current_vertex[0]][current_vertex[1]] = new_color
​
     # Queue up the neighbors:
 row = current_vertex[0]
  col = current_vertex[1]
   neighbors = []
    if row - 1 >= 0 and image[row-1][col] == current_color:
         # look UP
        neighbors.append((row - 1, col))
    if row + 1 < len(image) and image[row+1][col] == current_color:
        # look down
        neighbors.append((row + 1, col))
    if col - 1 >= 0 and image[row][col-1] == current_color:
        # look left
        neighbors.append((row, col - 1))
    if col + 1 < len(image[row]) and image[row][col+1] == current_color:
        # look right
        neighbors.append((row, col + 1))
​
 for neighbor in neighbors:
      queue.append(neighbor)
​
​
​
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
​
flood_fill(image, 1, 1, 2)
​
for i in image:
    print(i)


"""________________________________________________________________________________________________
                        UNDERSTANDING:
___________________________________________________________________________________________________
______Problem______
-drop color
-begins to propogate
-each node propogates

-fill neighbors to change value (coordinate increment)
            -neighbors with same value


"start-end"  =  traverse =  graph







_____Map/Chart/Graph______
build graph

vertex =  pixels
edge =   neighbors (with equal value)





________Tools________
-representation                 Matrix  (vertex = pixels)    
                                    (pixel = coordinate)    
                    
-data structure                 Stack
-search/Traversal algorithm     DFS (queue) a number with vertex(row, column)
                                        (memorize queue structure)

______Structure/Plan________
Build Graph
-
-
-
-

Traverse it
-traverse (define traversal, visited, addVertexOrder FIFO)
-queue
-pop item off queue
- check if vertex was visisted
- do something to vertex    (update pixel color)   ()
- queue up the neighbors:   
            define,  vertex, edges/neighbor,  
            update   vertex  (if/else)       
                     next/neighbor  (must define current color)
                                    (up, down, left, right   =  matrix)       increment coordinates
- loop append(neighbor)/next
- return None   (or image)

 



__________________________________________________________________________________________________ 
                        PSUEDO CODE:
__________________________________________________________________________________________________                        





"""
# ________________________________________________________________________________________________________
#                                       Matrix #2
# ________________________________________________________________________________________________________

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



def get______(self):
    return self.vertices[v1].add_connection(self.vertices[v2], weight)


def get_vertices(self):
    return self.vertices.keys()

def breadth_first_search(self, starting_vert):
    to_visit = Queue()
    visited = set()
    to_visit.enqueue(starting_vert)
    visited.add(starting_vert)
    while to_visit.size() > 0:
        current_vert = to_visit.dequeue()
        for next_vert in current_vert.get_connections():
            if next_vert not in visited:
                visited.add(next_vert)

