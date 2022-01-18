"""
Problem statement:
Compute the nth Fibonacci number.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def fib(n):
    """
    Given a fibonacci series index, returns the value of a number from the fibonacci series.
    Does not incorporate caching/memoization.
    """

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 2) + fib(n - 1)


# //----------------------------------------------------------------------------------//
# //
# //


def fib_cached_rec(n, memo):  # test
    """
    Given a fibonacci series index, returns the value of a number from the fibonacci series.
    With caching/memoization.
    """

    if n < len(memo):
        return memo[n]
    else:
        memo.append(fib_cached_rec(n - 2, memo) + fib_cached_rec(n - 1, memo))
        return memo[n]


def fib_cached(n):
    memo = [0, 1]
    return fib_cached_rec(n, memo)


# //----------------------------------------------------------------------------------//
# //
# //


def fib_book_init(n):
    return fib_book(n, [0] * (n + 1))


def fib_book(i, memo):
    """
    Book solution: top-down approach
    """

    if i == 0 or i == 1:
        return i

    if memo[i] == 0:
        memo[i] = fib_book(i - 2, memo) + fib_book(i - 1, memo)

    return memo[i]


# //----------------------------------------------------------------------------------//
# //
# //


def fib_book_bottom_up(n):
    """
    Book solution: bottom-up approach
    """
    memo = [0, 1]
    for i in range(2, n + 1):
        memo.append(memo[i - 2] + memo[i - 1])

    return memo[n]


# //----------------------------------------------------------------------------------//
# //
# //


def fib_book_bottom_up_improved(n):
    """
    Book solution: bottom-up approach, memory improvement
    """
    a = 0
    b = 1
    c = None

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return c


# //***************************************************************************************//
# //
# //


def main():
    print(fib(7))
    print(fib_cached(7))
    print(fib_book_init(7))
    print(fib_book_bottom_up(7))
    print(fib_book_bottom_up_improved(7))


if __name__ == "__main__":
    main()
