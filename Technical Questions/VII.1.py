"""
Problem statement:
Print all positive integer solutions to the equation a^3+b^3=c^3+d^3, where a, b, c,
and d are integers between 1 and 1000.
"""

# //----------------------------------------------------------------------------------//
# //
# //
def Print_Integers(n):
    map_of_vals = {}
    for c in range(1, n):
        for d in range(1, n):
            val = pow(c, 3) + pow(d, 3)
            if val in map_of_vals:
                map_of_vals[val].append((c, d))
            elif val not in map_of_vals:
                map_of_vals[val] = [(c, d)]

    for val in map_of_vals:
        for pair1 in map_of_vals[val]:
            for pair2 in map_of_vals[val]:
                print(pair1, pair2)


# //***************************************************************************************//
# //
# //


def main():
    print(Print_Integers(1000))


if __name__ == "__main__":
    main()
