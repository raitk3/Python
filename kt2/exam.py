"""KT2."""


def last_to_first(s):
    """
    Move last symbol to the beginning of the string.

    last_to_first("ab") => "ba"
    last_to_first("") => ""
    last_to_first("hello") => "ohell"
    """

    if len(s) == 0:
        return ""
    return s[-1] + s[0:-1]


def have_seven(nums):
    """
    Given a list if ints, return True if the value 7 appears in the list exactly 3 times.

    No consecutive elements shall have the same value.

    have_seven([1, 2, 3]) => False
    have_seven([7, 1, 7, 7]) => False
    have_seven([7, 1, 7, 1, 7]) => True
    have_seven([7, 1, 7, 1, 1, 7]) => False
    """
    seven_count = 0
    prev_num = None
    for num in nums:
        if num == prev_num:
            return False
        if num == 7:
            seven_count += 1
        prev_num = num

    return seven_count == 3


def g_happy(s):
    """
    We'll say that a lowercase 'g' in a string is "happy" if there is another 'g' immediately to its left or right.

    Return True if all the g's in the given string are happy.

    gHappy("xxggxx") => True
    gHappy("xxgxx") => False
    gHappy("xxggyygxx") => False
    """
    index_of_char_in_for_atm = 0
    happy_g = False
    no_lonely_g = True
    if len(s) < 2:
        return False
    for el in s:
        if el == "g":
            if index_of_char_in_for_atm == 0:
                if s[index_of_char_in_for_atm + 1] == "g":
                    happy_g = True
                else:
                    no_lonely_g = False
            elif index_of_char_in_for_atm == len(s) - 1:
                if s[index_of_char_in_for_atm - 1] == "g":
                    happy_g = True
                else:
                    no_lonely_g = False
            elif (s[index_of_char_in_for_atm - 1] != "g" and s[index_of_char_in_for_atm + 1] != "g")\
                    or (s[index_of_char_in_for_atm - 1] == "g" and s[index_of_char_in_for_atm + 1] == "g"):
                no_lonely_g = False
            elif s[index_of_char_in_for_atm - 1] == "g" or s[index_of_char_in_for_atm + 1] == "g":
                happy_g = True
        index_of_char_in_for_atm += 1
    return happy_g and no_lonely_g


if __name__ == '__main__':
    assert last_to_first("HellNoO") == "OHellNo"
    assert last_to_first("kakdisjfosdf") == "fkakdisjfosd"
    assert last_to_first("") == ""
    assert last_to_first("1234567890") == "0123456789"
    assert have_seven([1, 2, 3]) is False
    assert have_seven([7, 1, 7, 7]) is False
    assert have_seven([7, 1, 7, 1, 7]) is True
    assert have_seven([7, 1, 7, 1, 1, 7]) is False
    assert have_seven([0, 3, 4, 2, 4, 5, 7, 4, 2, 5, 7, 5, 7, 5, 3, 1, 2]) is True
    assert g_happy("xxggxx") is True
    assert g_happy("xxgxx") is False
    assert g_happy("xxggyygxx") is False
    assert g_happy("g, gg, ggg") is False
    assert g_happy("") is False
    assert g_happy("0123456789") is False
    assert g_happy("ggga") is False
    assert g_happy("01gg23gg") is True
    assert g_happy("aga mina ei tea, mis sel viga on") is False
    assert g_happy("random text") is False
    assert g_happy("ggg") is False
