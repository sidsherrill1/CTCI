"""
Problem statement:
Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents),
and pennies (1 cent), write code to calculate the number of ways of representing n cents.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def rep_rec(cents, coin_sizes, i):
    c = coin_sizes[i]

    if i == len(coin_sizes) - 1:
        if cents % c == 0:
            return 1
        else:
            return 0

    ways = 0
    for amount in range(0, cents + 1, c):
        ways += rep_rec(cents - amount, coin_sizes, i + 1)
    return ways


def rep(cents):
    coin_sizes = [25, 10, 5, 1]
    return rep_rec(cents, coin_sizes, 0)


# //***************************************************************************************//
# //
# //


def main():
    print(rep(5))


if __name__ == "__main__":
    main()
