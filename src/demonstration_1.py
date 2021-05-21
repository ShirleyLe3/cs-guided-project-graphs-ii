
# --------------------------------------------------------------------
#                       Adjacent List
# ____________________________________________________________________

graph = {
    'a': set(['b', 'c', 'd']),
    'b': set(),
    'c': set('e'),
    'd': set(['e', 'f']),
    'e': set(['a', 'f']),
    'f': set(),
}
​
# def main_function(current_vertex):
#     visited = set()
#     def print_graph(current_vertex):
#         print(current_vertex)
#         visited.add(current_vertex)
#         # Recurse on the children
#         for neighbor in graph[current_vertex]:
#             if neighbor not in visited:
#                 print_graph(neighbor)

#     print_graph(current_vertex)
​
​


def print_graph(current_vertex, visited):
    print(current_vertex)
    visited.add(current_vertex)
    print(visited)
    # Recurse on the children
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            print_graph(neighbor, visited)


​


def iterative_dfs(start_vertex, target_vertex):
    stack = []
    stack.append((start_vertex, []))
    visited = set()


​
while len(stack) > 0:
    # process vertices on the stack, and queue up other ones
    current_vertex, current_path = stack.pop()
    visited.add(current_vertex)
​
current_path.append(current_vertex)
​
# Check if the current vertex is our target
if current_vertex == target_vertex:
    print("Found")
    return current_path
​
for neighbor in graph[current_vertex]:
    if neighbor not in visited:
        stack.append((neighbor, current_path.copy))
​

​
# print(iterative_dfs('a', 'f'))
​


def iterative_bfs(start_vertex, target_vertex):
    queue = []
    queue.append((start_vertex, []))
    visited = set()


​
while len(queue) > 0:
    # process vertices on the stack, and queue up other ones
    current_vertex, current_path = queue.pop(0)
    # if current_vertex in visited:
    #     continue
​
visited.add(current_vertex)
current_path.append(current_vertex)
​
# Check if the current vertex is our target
if current_vertex == target_vertex:
    print("Found")
    return current_path
​
for neighbor in graph[current_vertex]:
    queue.append((neighbor, current_path.copy()))
​
​
print(iterative_bfs('a', 'f'))


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
