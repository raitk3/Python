# -*- coding: utf-8 -*-
"""Check if given ID code is valid."""


def is_valid_gender_number(gender_number):
    """Check if gender number is valid."""
    return 1 <= gender_number <= 6


def is_leap_year(leap_year):
    """Check if a year is leap year."""
    if leap_year % 400 == 0:
        return True
    elif leap_year % 100 == 0:
        return False
    elif leap_year % 4 == 0:
        return True
    else:
        return False


def get_gender(gender_number: int):
    """Check if a person is male or female."""
    if gender_number in [2, 4, 6]:
        return "female"
    elif gender_number in [1, 3, 5]:
        return "male"


def is_valid_year_number(year_number: int) -> bool:
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    return 0 <= year_number <= 99


def is_valid_month_number(month_number: int) -> bool:
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    return 1 <= month_number <= 12


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """
    Check if given value is correct for day number in ID code.

    Also, consider leap year and which month has 30 or 31 days.

    :param gender_number: int
    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean

    """
    if month_number == 2:
        if is_leap_year(get_full_year(gender_number, year_number)):
            return day_number in range(0, 30)
        else:
            return day_number in range(0, 29)

    elif month_number in range(1, 8):
        if month_number % 2 == 0:
            return day_number in range(0, 31)
        else:
            return day_number in range(0, 32)
    elif month_number in range(8, 13):
        if month_number % 2 == 0:
            return day_number in range(0, 32)
        else:
            return day_number in range(0, 31)
    else:
        return False


def is_valid_birth_number(birth_number: int):
    """
    Check if given value is correct for birth number in ID code.

    :param birth_number: int
    :return: boolean
    """
    return 1 <= birth_number <= 999


def is_valid_control_number(id_code: str) -> bool:
    """
    Check if given value is correct for control number in ID code.

    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean

    """
    total_1 = int(id_code[0]) * 1 + int(id_code[1]) * 2 + int(id_code[2]) * 3 + int(id_code[3]) * 4 +\
        int(id_code[4]) * 5 + int(id_code[5]) * 6 + int(id_code[6]) * 7 + int(id_code[7]) * 8 + int(id_code[8]) * 9 +\
        int(id_code[9]) * 1
    total_2 = int(id_code[0]) * 3 + int(id_code[1]) * 4 + int(id_code[2]) * 5 + int(id_code[3]) * 6\
        + int(id_code[4]) * 7 + int(id_code[5]) * 8 + int(id_code[6]) * 9 + int(id_code[7]) * 1 + int(id_code[8]) * 2\
        + int(id_code[9]) * 3
    result_1 = total_1 % 11
    result_2 = total_2 % 11
    if result_1 != 10:
        return result_1 == int(id_code[10])
    else:
        if result_2 == 10:
            return result_2 == 0
        else:
            return result_2 == int(id_code[10])


def get_full_year(gender_number: int, year_number: int) -> int:
    """
    Define the 4-digit year when given person was born.

    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year_number: int
    :return: int

    """
    if gender_number in range(1, 3):
        return 1800 + year_number
    elif gender_number in range(3, 5):
        return 1900 + year_number
    else:
        return 2000 + year_number


def get_birth_place(birth_number: int) -> str:
    """
    Find the place where the person was born.

    Possible locations are following: Kuressaare, Tartu, Tallinn, Kohtla-Järve, Narva, Pärnu,
    Paide, Rakvere, Valga, Viljandi, Võru and undefined. Lastly if the number is incorrect the function must return
    the following 'Wrong input!'
    :param birth_number: int
    :return: str
    """
    birth_place = {(1, 11): "Kuressaare",
                   (11, 21): "Tartu",
                   (21, 221): "Tallinn",
                   (221, 271): "Kohtla-Järve",
                   (221, 371): "Tartu",
                   (371, 421): "Narva",
                   (421, 471): "Pärnu",
                   (471, 491): "Tallinn",
                   (491, 521): "Paide",
                   (521, 571): "Rakvere",
                   (571, 601): "Valga",
                   (601, 651): "Viljandi",
                   (651, 711): "Võru",
                   (711, 1000): "undefined"}
    for city in birth_place:
        if birth_number in range(city[0], city[1]):
            return birth_place[city]
    return "Wrong input!"


def get_data_from_id(id_code: str) -> str:
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a <gender> born on <DD.MM.YYYY> in <location>.
    :param id_code: str
    :return: str
    """
    if is_id_valid(id_code):
        return f"This is a {get_gender(int(id_code[0]))} born on {id_code[5:7]}.{id_code[3:5]}." \
            f"{get_full_year(int(id_code[0]), int(id_code[1:3]))}" \
            f" in {get_birth_place(int(id_code[7:10]))}"
    else:
        return "Given invalid ID code!"


def is_id_valid(id_code: str) -> bool:
    """
    Check if given ID code is valid and return the result (True or False).

    Complete other functions before starting to code this one.
    You should use the functions you wrote before in this function.
    :param id_code: str
    :return: boolean
    """
    return len(id_code) == 11 and is_valid_gender_number(int(id_code[0])) and is_valid_year_number(int(id_code[1:3]))\
        and is_valid_month_number(int(id_code[3:5]))\
        and is_valid_day_number(get_full_year(int(id_code[0]), int(id_code[1:3])), int(id_code[5:7]), int(id_code[0]),
                                int(id_code[3:5]))\
        and is_valid_birth_number(int(id_code[7:10])) and is_valid_control_number(id_code)
# int(id_code[5:7]), int(id_code[0]), int(id_code[3:5]), get_full_year(int(id_code[0]), int(id_code[1:3])


if __name__ == '__main__':
    print(get_data_from_id("39708060036"))
