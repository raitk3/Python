"""Recursion."""


def recursive_sum(numbers: list) -> int:
    """
    Find out the sum of all the even numbers using recursion.

    :param numbers: list of randomly ordered numbers
    :return: sum of even numbers
    """
    if len(numbers) == 1:
        if numbers[0] % 2 == 0:
            return numbers[0]
        else:
            return 0
    else:
        if numbers[0] % 2 == 0:
            return numbers[0] + recursive_sum(numbers[1:])
        else:
            return recursive_sum(numbers[1:])


def loop_sum(numbers: list) -> int:
    """
    Find out the sum of all the even numbers using loops.

    :param numbers: list of randomly ordered numbers
    :return: sum of even numbers
    """
    total = 0
    for el in numbers:
        if el % 2 == 0:
            total += el
    return total


def loop_reverse(s: str) -> str:
    """Reverse a string using a loop.

    :param s: string
    :return: reverse of s
    """
    new_s = ""
    for char in s:
        new_s = char + new_s
    return new_s


def recursive_reverse(s: str) -> str:
    """Reverse a string using recursion.

    :param s: string
    :return: reverse of s
    """
    if s == "":
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]


if __name__ == '__main__':
    print(recursive_sum([1, 3, 5, 7, 9]))
    print(recursive_sum([2, 4, 5, 8]))
    print(loop_sum([1, 3, 5, 7, 9]))
    print(loop_sum([2, 4, 5, 8]))
    print(recursive_reverse("abcdef"))
    print(loop_reverse("abcdef"))
