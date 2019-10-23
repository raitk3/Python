"""Test 2 (N8)."""


def make_ends(nums):
    """
    Given an array of ints, return a new array length 2 containing the first and last elements from the original array.

    The original array will be length 1 or more.

    make_ends([1, 2, 3]) → [1, 3]
    make_ends([1, 2, 3, 4]) → [1, 4]
    make_ends([7, 4, 6, 2]) → [7, 2]

    :param nums: List of integers.
    :return: List with the first and the last element from the input list.
    """
    return [nums[0], nums[-1]]


def caught_speeding(speed, is_birthday):
    """
    Return which category speeding ticket you would get.

    You are driving a little too fast, and a police officer stops you.
    Write code to compute the result, encoded as an int value:
    0=no ticket, 1=small ticket, 2=big ticket.
    If speed is 60 or less, the result is 0.
    If speed is between 61 and 80 inclusive, the result is 1.
    If speed is 81 or more, the result is 2.
    Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

    caught_speeding(60, False) → 0
    caught_speeding(65, False) → 1
    caught_speeding(65, True) → 0

    :param speed: Speed value.
    :param is_birthday: Whether it is your birthday (boolean).
    :return: Which category speeding ticket you would get (0, 1, 2).
    """
    if is_birthday is True:
        speed -= 5

    if speed <= 60:
        return 0
    elif 60 < speed <= 80:
        return 1
    else:
        return 2


def combo_string(s1, s2):
    """
    Return a new string of the form short + long + short.

    Given 2 strings, a and b, return a string of the form short+long+short,
    with the shorter string on the outside and the longer string on the inside.
    The strings will not be the same length, but they may be empty (length 0).

    combo_string('Hello', 'hi') → 'hiHellohi'
    combo_string('hi', 'Hello') → 'hiHellohi'
    combo_string('aaa', 'b') → 'baaab'

    :param s1:
    :param s2:
    :return:
    """
    if len(s1) == 0 or len(s2) == 0:
        return s1 or s2
    if len(s1) < len(s2):
        return s1 + s2 + s1
    elif len(s1) > len(s2):
        return s2 + s1 + s2


def min_index_value(nums):
    """
    Take the first and the last element as indices of two elements and return the smaller of those elements.

    If at least one index is out of range, return -1.
    All the values are non-negative integers.

    min_index_value([1, 2, 3]) => -1 (3 is out of range)
    min_index_value([1, 2, 1]) => 2 (both elements point to 2)
    min_index_value([1, 2, 0]) => 1 (have to take minimum of 2 and 1)

    :param nums: List of non-negative integers.
    :return: Minimum value of two elements at positions of the first and the last element value.
    """
    el_1 = nums[0]
    el_2 = nums[-1]
    if 0 < el_1 >= len(nums) or 0 < el_2 >= len(nums):
        return -1
    else:
        comp_el_1 = nums[el_1]
        comp_el_2 = nums[el_2]
        return min(comp_el_1, comp_el_2)


def max_duplicate(nums):
    """
    Return the largest element which has at least one duplicate.

    If no element has duplicate element (an element with the same value), return None.

    max_duplicate([1, 2, 3]) => None
    max_duplicate([1, 2, 2]) => 2
    max_duplicate([1, 2, 2, 1, 1]) => 2

    :param nums: List of integers
    :return: Maximum element with duplicate. None if no duplicate found.
    """
    check_list = []
    new_list = []
    for el in nums:
        if el in check_list:
            new_list.append(el)
        else:
            check_list.append(el)

    if len(new_list) == 0:
        return None
    else:
        return max(new_list)


if __name__ == '__main__':
    print(make_ends([1, 2, 3]))
    print(make_ends([2, 3, 4, 5, 3, 2, 1]))
    print(caught_speeding(50, False))
    print(caught_speeding(64, True))
    print(combo_string("t", "uu"))
    print(combo_string("teet", "tuu"))
    print(combo_string("", ""))
    print(min_index_value([1, 2, 3]))
    print(min_index_value([1, 2, 2]))
    print(min_index_value([1, 2, 1]))
    print(max_duplicate([1, 2, 3, 1]))
    print(max_duplicate([1, 2, 3, 1, 4, 5, 5]))
