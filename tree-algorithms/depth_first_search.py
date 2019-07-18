# pseudo code taken from CLRS book

# vertices is list of vertex in graph : [0, 1, 2, 3 ...] (must be continuous)
# adjacencyList is the list whose 'i'th element is list of vertices adjacent to vertex i

time = 0;

class vertex:
    def __init__(self, adjVertices, color='White', parent='None', discovery_time=float('inf'), finishing_time=float('inf')):
        self.adjVertices = adjVertices;
        self.color = color;
        self.parent = parent;
        self.discovery_time = discovery_time;
        self.finishing_time = finishing_time;

def DFS(vertices, adjacencyList):
    global time
    
    vertices_objects = [ vertex(adjacencyList[v]) for v in vertices ]

    time = 0
    
    for vert in vertices:
        if vertices_objects[vert].color == 'White':
            DFS_Visit(vert, vertices_objects, adjacencyList)

    return vertices_objects

def DFS_Visit(vertex, vertices, adjacencyList):
    vertex_object = vertices[vertex]

    vertex_object.color = 'Gray' # Vertex just been discovered
    global time
    time = time + 1
    vertex_object.discovery_time = time;

    for vert in adjacencyList[vertex]:
        if vertices[vert].color == 'White':
            vertices[vert].parent = vertex
            DFS_Visit(vert, vertices, adjacencyList)

    vertex_object.color = 'Black' # Discovery of this vertex has been finished

    time = time + 1
    vertex_object.finishing_time = time
    
    

