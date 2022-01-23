"""
Problem statement:
The Heavy Pill: You have 20 bottles of pills. 19 bottles have 1.0gram pills, but one has
pills of weight 1.1 grams. Given a scale that provides an exact measurment, how would
you find the heavy bottle? You can only use the scale once

"""

# //----------------------------------------------------------------------------------//
# //
# //


def Find_Heavy_Bottle(num_bottles, total_weight):
    num_pills = 0
    for i in range(1, num_bottles + 1):
        num_pills += i
    # If weight was 20.1 and pills added was 20, we'd know the pill bottle that had only
    # one pill in the pile was from the bottle of heavier pills
    num_pills = float(num_pills)
    diff = (total_weight - num_pills) * 10
    return round(diff, 0)


# //***************************************************************************************//
# //
# //


def main():
    print(Find_Heavy_Bottle(3, 6.3))


if __name__ == "__main__":
    main()
