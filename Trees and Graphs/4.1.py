"""
Problem statement:
Given a directed graph and two nodes (S and E), design an algorithm to find out weather
there is a route from S to E.
"""

# //----------------------------------------------------------------------------------//
# //
# //


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []


def Route_Exists(n1, n2):
    if n1 == n2:
        return True

    if len(n1.children) == 0:
        return False

    for child in n1.children:
        if Route_Exists(child, n2):
            return True

    return False


# //***************************************************************************************//
# //
# //


def main():
    A = Node(1)
    B = Node(2)
    C = Node(3)
    S = Node(4)
    E = Node(5)

    A.children.append(B)
    S.children.append(B)
    B.children.append(C)
    B.children.append(E)

    print(Route_Exists(S, E))


if __name__ == "__main__":
    main()
