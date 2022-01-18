"""
Problem statement:
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits"
such that the robot cannot step on them. Design an algorithm to find a path for the robot from 
the top left to the bottom right.
"""

# //----------------------------------------------------------------------------------//
# //
# //


class Point:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __eq__(self, obj):
        return self.r == obj.r and self.c == obj.c

    def __str__(self):
        return f"{self.r},{self.c}"


def Get_Path(maze):
    if maze == None or len(maze) == 0:
        return None
    path = []
    dead_ends = []
    if Find_Path(len(maze) - 1, len(maze[0]) - 1, maze, path, dead_ends):
        return path
    else:
        return None


def Find_Path(r, c, maze, path, dead_ends):
    if r < 0 or c < 0 or not maze[r][c]:
        return False

    p = Point(r, c)
    if p in dead_ends:
        return False

    at_origin = r == 0 and c == 0
    if at_origin or Find_Path(r - 1, c, maze, path, dead_ends) or Find_Path(r, c - 1, maze, path, dead_ends):
        path.append(p)
        return True
    else:
        dead_ends.append(p)
        return False


# //***************************************************************************************//
# //
# //


def main():
    maze = [
        [True, False, True, True, True],
        [True, True, False, True, True],
        [True, True, True, True, True],
        [True, True, True, False, True],
        [True, True, True, True, True],
    ]
    path = Get_Path(maze)
    for p in path:
        print(p)


if __name__ == "__main__":
    main()
