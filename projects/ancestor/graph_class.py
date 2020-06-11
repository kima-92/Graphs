
from util import Queue, Stack

"""

# Queue

class Queue():
    def __init__(self):
        self.queue = []    
    
    def enqueue(self, value):
        self.queue.append(value)    
    
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None    
            
    def size(self):
        return len(self.queue)
        """

# Graphs


#  ** Sets don't have duplicates

class Graph:

    def __init__(self):
        self.vertices = {}


    # Add verts
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()     # an empty set of edges, from this vert

    # Add edges
    # This adds a edge in one direction
    def add_edge(self, v1, v2):
        
        if v1 and v2 in self.vertices:
            self.vertices[v1].add(v2)   # add v2 as a neigbor to v1
        else:
            raise IndexError(f"Can not create edge between {v1} and {v2}")


    # Get neighbors for a vert
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]  # It will return the value, which will be a set of all the neighbors

    def bft(self, starting_verting_vertex_id):   # Breath First Traversal

        q = Queue()
        q.enqueue(starting_verting_vertex_id)

        # Create a Set to store visited vertices
        visited = set()

        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()

            # If that vertice has not been visited...
            if v not in visited:
                # Visit it
                print(v)

                # Mark it as visited...
                visited.add(v)

                # For add all of it's neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    # def bfs(self, starting_vertex_id, target_vertex_id):
    # ** Depth First Traversal is missing
    # ** You would use pop instead of dequeue and push instead of enqueue


