from graph import Vertex, Edge

def topological_sort(vertices):
    sorted = []
    top = []

    for vert in vertices:
        if len(vert.in_edges) == 0:
            top.append(vert) 

    while len(top) != 0:
        curr = top.pop()
        sorted.append(curr)

        for edge in curr.out_edges:

            if edge.from_vertex == curr:
                top.append(edge.to_vertex)
            edge.destroy()

    if len(sorted) > len(vertices):
        return [] 

    return sorted