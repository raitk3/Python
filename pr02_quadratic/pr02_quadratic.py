"""Quadratic equation."""

import math


def find_roots(a, b, c):
    """See teeb ruutvõrrandit..."""
    d = (b**2 - 4 * a * c)
    if d == 0:
        x = (-1 * b) / (2 * a)
        print("Solution is " + str(x))

    elif d < 0:
        print("No solutions")
    elif a == 0:
        x = (-c / b)
        print("Solution is " + str(x))
    else:
        x1 = ((-1 * b - math.sqrt(d)) / (2 * a))
        x2 = ((-1 * b + math.sqrt(d)) / (2 * a))
        x1 = round(x1, 1)
        x2 = round(x2, 1)
        print("Solutions are " + str(x1) + " and " + str(x2))


if __name__ == "__main__":
    find_roots(1, 0, -1)
    find_roots(1, 0, 0)
    find_roots(1, 0, 1)
    find_roots(0, 0.5, 1)
