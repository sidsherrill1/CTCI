"""
Problem statement:
Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and 
a new color, fill in the surrounding area until the color changes from the original color.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def paint_fill_rec(screen, point_r, point_c, new_color, old_color):

    if len(screen) <= point_r or point_r < 0 or len(screen[0]) <= point_c or point_c < 0:
        return

    if screen[point_r][point_c] != old_color:
        return

    screen[point_r][point_c] = new_color
    paint_fill_rec(screen, point_r - 1, point_c, new_color, old_color)
    paint_fill_rec(screen, point_r + 1, point_c, new_color, old_color)
    paint_fill_rec(screen, point_r, point_c - 1, new_color, old_color)
    paint_fill_rec(screen, point_r, point_c + 1, new_color, old_color)
    return screen


def paint_fill(screen, point, new_color):
    point_c = point[0]
    point_r = point[1]
    old_color = screen[point_r][point_c]
    screen = paint_fill_rec(screen, point_r, point_c, new_color, old_color)
    return screen


# //***************************************************************************************//
# //
# //


def main():
    screen = [
        ["blue", "black", "black", "black"],
        ["blue", "orange", "black", "black"],
        ["blue", "black", "black", "black"],
        ["blue", "black", "green", "black"],
    ]
    point = [2, 1]
    new_color = "pink"
    new_screen = paint_fill(screen, point, new_color)
    for r in new_screen:
        print(r)


if __name__ == "__main__":
    main()
