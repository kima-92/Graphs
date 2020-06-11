from util import Stack, Queue 
from graph_class import Graph

def earliest_ancestor(ancestors, starting_node):

    graph = Graph()

    # For each pair
    for i in ancestors:
        # Add a vertices
        graph.add_vertex(i[0])  # Parent
        graph.add_vertex(i[1])  # Child

        # Add an edge between the parent and the child
        graph.add_edge(i[1],i[0])

    q = Queue()
    visited = set()

    longest_path = 1
    parent_end = -1

    q.enqueue([starting_node])

    while q.size() > 0:

        path = q.dequeue()
        vertex = path[-1]

        if len(path) >= longest_path and vertex < parent_end or len(path) > longest_path:
            parent_end = vertex
            visited.add(vertex)

        for neighbor in graph.vertices[vertex]:
                path_add = path.copy()
                path_add.append(neighbor)
                q.enqueue(path_add)

    return parent_end




