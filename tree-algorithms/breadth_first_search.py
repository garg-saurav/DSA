# pseudo code taken from CLRS book

# vertices is list of vertex in graph : [0, 1, 2, 3 ...] (must be continuous)
# source is the source vertex number
# adjacencyList is the list whose 'i'th element is list of vertices adjacent to vertex i

from collections import deque

class vertex:
    def __init__(self, adjVertices, color='White', parent='None', distance=float('inf')):
        self.adjVertices = adjVertices;
        self.color = color;
        self.parent = parent;
        self.distance = distance;

def BFS (source, vertices, adjacencyList):
    vertices = [ vertex(adjacencyList[v]) for v in vertices ]
    # now vertices contains list of vertex objects

    vertices[source].color = 'Gray'
    vertices[source].distance = 0

    Q = deque() #Q is the queue consisting of 'Gray' vertices
    Q.append(source)

    while len(Q) != 0:
        v = Q.popleft()
        vert = vertices[v]
        for adj in adjacencyList[v]:
            adj_vertex = vertices[adj]
            if adj_vertex.color == 'White': # not yet visited
                adj_vertex.color = 'Gray'
                adj_vertex.distance = vert.distance + 1
                adj_vertex.parent = v
                Q.append(adj)
        vert.color = 'Black'
    return vertices

def print_path(source, vertices, vertex):
    # Here this vertices is the output of BFS
    # Assumes BFS has already been run

    parent = vertices[vertex].parent

    if vertex == source:
        print (source, end=' ')
        
    elif parent == None:
        print ("No path from", source, "to", vertex, "exists")

    else:
        print_path(source, vertices, parent)
        print (vertex, end=' ')


    
    
    
    
