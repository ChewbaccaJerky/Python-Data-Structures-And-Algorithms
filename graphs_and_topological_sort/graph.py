class Vertex:

    def __init__(self, value):
        self.value = value
        self.in_edges = []
        self.out_edges = []

class Edge:
    
    def __init__(self, from_vertex, to_vertex, cost = 1):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.cost = cost
        to_vertex.in_edges.append(self)
        from_vertex.out_edges.append(self)

    def destroy(self):
        self.to_vertex.to_edges.delete(self)
        self.to_vertex.out_edges.delete(self)
        self.from_vertex.out_edges.delete(self)
        self.from_vertex.in_edges.delete(self)
        self.from_vertex = None
        self.to_vertex = None