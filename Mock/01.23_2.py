"""
Problem statement:
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""

# //----------------------------------------------------------------------------------//
# //
# //


class Node:
    def __init__(self, vertex, adjacentLength):
        self.adjacent = [0] * adjacentLength
        self.vertex = vertex
        self.adjacentCount = 0
        self.visited = False

    def add_adjacent(self, x):
        if self.adjacentCount < len(self.adjacent):
            self.adjacent[self.adjacentCount] = x
            self.adjacentCount += 1
        else:
            print("No more adjacent nodes can be added")

    def get_adjacent(self):
        return self.adjacent

    def get_vertex(self):
        return self.vertex


class Graph:
    def __init__(self):
        self.max_vertices = 7
        self.vertices = []
        self.vertex_data = [""] * self.max_vertices
        self.count = 0

    def add_node(self, x: Node):
        if self.count < self.max_vertices:
            # check if the node is already in the graph
            if x.vertex in self.vertex_data:
                return False
            self.vertices.append(x)
            self.vertex_data[self.count] = x.vertex


def breadth_first_search(start, end):

    start.visited = True

    if start == end:
        return True

    if start.adjacentCount == 0:
        return False

    if end in start.adjacent:
        return True

    for node in start.adjacent:
        if node.visited:
            continue
        if breadth_first_search(node, end):
            return True

    return False


# //***************************************************************************************//
# //
# //


#            a ---> d ----> e ---> f
#            | \    |      |
#           v   \   |      v
#           b    v  v      g ---> i
#                 c
#                  \
#                   \
#                    h


def main():
    a_node = Node("a", 3)
    b_node = Node("b", 0)
    c_node = Node("c", 0)
    d_node = Node("d", 2)
    e_node = Node("e", 2)
    f_node = Node("f", 0)
    g_node = Node("g", 0)

    a_node.add_adjacent(b_node)
    a_node.add_adjacent(c_node)
    a_node.add_adjacent(d_node)
    d_node.add_adjacent(e_node)
    d_node.add_adjacent(c_node)
    e_node.add_adjacent(f_node)
    e_node.add_adjacent(g_node)

    print(breadth_first_search(a_node, a_node))
    print(breadth_first_search(a_node, c_node))
    print(breadth_first_search(b_node, c_node))
    print(breadth_first_search(e_node, g_node))
    print(breadth_first_search(d_node, b_node))


if __name__ == "__main__":
    main()
