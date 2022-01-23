"""
Problem statement:
Implement the Sieve of Eratosthenes, which is a highly efficient way to generate
a list of primes.
"""

import math

# //----------------------------------------------------------------------------------//
# //
# //


def Cross_Off(flags, prime):
    for i in range(prime * prime, len(flags), prime):
        print(i)
        flags[i] = False


def Find_Next_Prime(prime, flags):
    prime += 1
    for i in range(prime, len(flags)):
        if flags[i] == True:
            return i


def Sieve_Of_Eratosthenes(max):
    flags = [True] * (max + 1)

    flags[0] = False
    flags[1] = False

    prime = 2
    while prime <= math.sqrt(max):
        Cross_Off(flags, prime)
        prime = Find_Next_Prime(prime, flags)

    primes = []
    for i in range(len(flags)):
        if flags[i]:
            primes.append(i)

    return primes


# //***************************************************************************************//
# //
# //


def main():
    print(Sieve_Of_Eratosthenes(100))


if __name__ == "__main__":
    main()
