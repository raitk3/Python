"""Common elements."""


def find_shortest_string(string_list):
    """
    Find and return the shortest string in list.

    If two strings are the same length return the one that comes first in the list.
    If the list is empty return none.
    :param string_list:
    :return: shortest string in list.
    """
    if len(string_list) > 0:
        return min(string_list, key=len)


def sort_list(string_list):
    """
    Sort list by the length of the strings in ascending order.

    This function must use find_shortest_string().
    :param string_list:
    :return: sorted list.
    """
    backup_list = string_list
    new_list = []
    while len(backup_list) > 0:
            shortest_string = find_shortest_string(backup_list)
            backup_list.remove(shortest_string)
            new_list.append(shortest_string)
    return new_list


def find_common_elements(first_list, second_list):
    """
    Find common elements from two lists.

    Make sure there are no duplicates in the result list.
    :param first_list:
    :param second_list:
    :return: Distinct common elements as a list.
    """
    new_list = []
    for el in first_list:
        if el in second_list and el not in new_list:
            new_list.append(el)
    return new_list


def find_common_elements_sorted(first_list, second_list):
    """
    Find common elements and then sort the list.

    Find common elements that exist in both lists. Make sure that there are also no repeating
    strings in the new list. Then sort the list by length. Shorter strings appearing first.
    This function must use sort_list().
    :param first_list:
    :param second_list:
    :return: sorted list.
    """
    common_elements = find_common_elements(first_list, second_list)
    sorted_elements = sort_list(common_elements)
    return sorted_elements


if __name__ == '__main__':
    list1 = ["aaa", "a", "a", "b", "c", "aaa"]
    list2 = ["a", "a", "bc", "cb", "aaa", "b", "aaaaa", "aa", "mmmmmmmmm", "v"]
    list3 = ["aaa", "b", "a"]
    list4 = ["aa", "aa", "aa"]
    list5 = ["aa", "aa", "aa"]
    print(find_common_elements(list1, list2))  # -> ['a', 'b', 'aaa']
    print(find_common_elements(list1, list3))
    print(find_common_elements_sorted(list1, list3))  # ->[]
    print(find_common_elements(list1, list4))
    print(find_common_elements_sorted(list4, list5))
    print(sort_list(list2))
