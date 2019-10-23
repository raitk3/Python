"""PR14."""


def segment_number(first_number, last_number):
    """
    Return list with elements dividable by 5 but not dividable by 3 between (inclusive) two arguments.

    Return list of numbers where only numbers between first_number
    and last_number (both inclusive) which divide by 5 but do not divide by 3
    are used.

    #1

    :param first_number: the lowest possible candidate
    :param last_number: the highest possible candidate
    :return: list of numbers
    """
    answer = []
    for xyz_number in range(first_number, last_number + 1):
        if xyz_number % 5 == 0 and xyz_number % 3 != 0:
            answer.append(xyz_number)
    return answer


def add_or_subtract(numbers):
    """
    Return the sum of all numbers in a list.

    The sum is calculated according to following rules:
        -always start by adding all the numbers together.
        -if you find a 0, start subtracting all following numbers until you find another 0, then start adding again.
        -there might be more than two 0 in a list - change +/- with every 0 you find.

    For example:
        [1, 2, 0, 3, 0, 4] -> 1 + 2 - 3 + 4 = 4
        [0, 2, 1, 0, 1, 0, 2] -> -2 - 1 + 1 - 2 = -4
        [1, 2] -> 1 + 2 = 3
        [4, 0, 2, 3] = 4 - 2 - 3 = -1

    #2

    :param numbers: the list of number given.
    :return: the sum of all numbers.
    """
    zero_count = 0
    sum = 0
    for num in numbers:
        if num == 0:
            zero_count += 1
        else:
            if zero_count % 2 == 0:
                sum += num
            elif zero_count % 2 == 1:
                sum -= num
    return sum


def should_get_up_early(is_weekday, really_tired, first_class_is_programming):
    """
    Decide if you should get up early.

    You should only even consider getting up early if it is a weekday, on weekends you should never get up early.
    If it is a weekday you should typically get up early, unless you are really tired.
    But if it is a weekday and you are really tired but the first class is a programming class you should still get up
    early ignoring you being tired.

    #3

    :param is_weekday: is it a weekday or not, boolean
    :param really_tired: are you really tired, boolean
    :param first_class_is_programming: is the first class a programming class, boolean
    :return: True if you should get up early, otherwise False
    """
    if is_weekday:
        if first_class_is_programming:
            return True
        else:
            if not really_tired:
                return True
    return False


def pear_fear(pears, people):
    """
    Return how many pears non-pear-fearers get.

    Every 3rd person fears pears, so they won't get any.
    How many pears will each get?
    Everyone who is not afraid of pears gets equal number of pears.
    Only whole pears will be used, so some pears may remain.

    #4

    :param pears:
    :param people:
    :return:
    """
    return pears // (people - int(people // 3))


def inverse_string(string):
    """Inverse that string."""
    if len(string) == 1:
        return string
    else:
        return inverse_string(string[1:]) + string[0]


def string_between_string(word1, word2):
    """
    Insert reversed word2 to the center of word1.

    word1 length is always even.

    #5

    :param word1: Initial word. String.
    :param word2: Word to reverse and insert. String.
    :return: New word as string.
    """
    if len(word1) == 0 and len(word2) > 0:
        return inverse_string(word2)
    elif len(word1) > 0 and len(word2) == 0:
        return word1
    elif len(word1) == 0 and len(word2) == 0:
        return ""
    else:
        return word1[0: int(len(word1) / 2)] + inverse_string(word2) + word1[int(len(word1) / 2):]


def get_padded_string(string1, string2):
    """
    Pad the longer of two strings with the shorter one on both sides.

    If both strings are the same length, consider string1 as the longer one.
    For example when string1 is "pizza" and string2 is "bbq", this should return "bbqpizzabbq".

    #6

    :param string1: String one
    :param string2:  String two
    :return: Padded string
    """
    if len(string1) > len(string2) or len(string1) == len(string2):
        return string2 + string1 + string2
    if len(string2) > len(string1):
        return string1 + string2 + string1


def remove_duplicate(number_list):
    """
    Return list where consecutive duplicates are removed.

    Go though given list and remove all
    occurrences of two or more of the same
    numbers appearing after one another.
    Remove all but one of the duplicates.

    #7

    :param number_list: input list
    :return: new list
    """
    answer = []
    for num in number_list:
        if len(answer) == 0 or num != answer[-1]:
            answer.append(num)
    return answer


def who_called(calls, name):
    """
    You are given a dictionary of calls and a name.

    Determine who called that name.
    If nobody called the person, return -1.

    #8

    :param calls: dictionary of all the calls
    :param name: name of the receiver
    :return: name of the caller
    """
    if len(calls) == 0:
        return -1
    else:
        for call in calls:
            if calls[call] == name:
                return call
        return -1


def remove_lowest_digit(number):
    """
    Given a non-negative integer, remove the first occurrence of the lowest digit and return a new number.

    123 => 23
    223 => 23
    232 => 32
    1 => 0

    :param number: non-negative integer
    :return: non-negative integer
    """
    if len(str(number)) == 1:
        return 0
    else:
        number_list_str = []
        number_list = [int(digit) for digit in str(number)]
        number_list.remove(min(number_list))
        for el in number_list:
            number_list_str.append(str(el))
        return int("".join(number_list_str))


def show_highest_grade(grade1, grade2):
    """
    Print "Highest grade: GRADE" where GRADE is the higher of two inputs.

    grade1, grade2 are both non-negative integers.

    3, 4 => "Highest grade: 4"

    #10

    :param grade1:
    :param grade2:
    :return:
    """
    if grade1 > grade2:
        print("Highest grade: " + str(grade1))
    else:
        print("Highest grade: " + str(grade2))


if __name__ == '__main__':

    assert segment_number(1, 11) == [5, 10]
    assert segment_number(1, 4) == []
    assert segment_number(-20, 20) == [-20, -10, -5, 5, 10, 20]

    assert add_or_subtract([1, 2, 0, 3]) == 0
    assert add_or_subtract([0, 1, 2]) == -3
    assert add_or_subtract([1, 2, 0, 2, 0, 4]) == 5

    assert should_get_up_early(True, True, True) is True
    assert should_get_up_early(False, True, False) is False

    assert pear_fear(10, 3) == 5
    assert pear_fear(10, 5) == 2
    assert pear_fear(0, 3) == 0
    assert pear_fear(17, 2) == 8
    assert pear_fear(21, 10) == 3

    assert string_between_string("ho", "lle") == "hello"
    assert string_between_string("", "yas") == "say"
    assert string_between_string("smrt", "a") == "smart"
    assert string_between_string("w  d", " ro ") == "w  or  d"
    assert string_between_string(".,", ",.") == "..,,"
    print(string_between_string("", ""))

    assert get_padded_string("pizza", "bbq") == "bbqpizzabbq"
    assert get_padded_string("dog", "cat") == "catdogcat"
    assert get_padded_string("geoff", "giraffe") == "geoffgiraffegeoff"

    assert remove_duplicate([1, 1, 2, 2, 3, 3]) == [1, 2, 3]
    assert remove_duplicate([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicate([1, 1, 1, 1, 1, 2, 1, 1, 3]) == [1, 2, 1, 3]

    assert who_called({}, "Nathan") == -1
    assert who_called({"Alex": "James", "Jeff": "Bill", "James": "Alex", "Daniel": "Matt"}, "Alex") == "James"
    assert who_called({"Alex": "James", "Jeff": "Bill", "James": "Alex", "Daniel": "Matt"}, "Olaf") == -1

    assert remove_lowest_digit(123) == 23
    assert remove_lowest_digit(100) == 10
    assert remove_lowest_digit(7) == 0
    assert remove_lowest_digit(171) == 71

    assert show_highest_grade(10, 14) is None
    # prints:
    # Highest grade: 14
