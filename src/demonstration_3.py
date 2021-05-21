"""Applications of BFS
Pathfinding, Routing
Find neighbor nodes in a P2P network like BitTorrent
Web crawlers
Finding people n connections away on a social network
Find neighboring locations on the graph
Broadcasting in a network
Cycle detection in a graph
Finding Connected Components (Links to an external site.)
Solving several theoretical graph problems
Coloring Vertexes
As we explore the graph, it is useful to color verts as we arrive at them and as we leave them behind as "already searched".

Unvisited verts are white, verts whose neighbors are being explored are gray, and verts with no unexplored neighbors are black.

Keeping Track of What We Need to Explore
In a BFS, it's useful to track which nodes we still need to explore. For example, in the diagram above, when we get to node 2, we know that we also need to explore nodes 3 and 4.

We can track that by adding neighbors to a queue (which remember is first in, first out), and then explore the verts in the queue one by one.

Follow Along
Pseudo-code for BFS
Let's explore some pseudo-code that shows a basic implementation of a breadth-first-search of a graph. Make sure you can read the pseudo-code and understand what each line is doing before moving on.

BFS(graph, startVert):
    for v of graph.vertexes:
        v.color = white

    startVert.color = gray
        queue.enqueue(startVert)

    while !queue.isEmpty():
        u = queue[0]  // Peek at head of the queue, but do not dequeue!

        for v of u.neighbors:
            if v.color == white:
                v.color = gray
                queue.enqueue(v)

        queue.dequeue()
        u.color = black

        """
