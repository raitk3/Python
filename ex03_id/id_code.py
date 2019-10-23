"""Check if given ID code is valid."""


def check_your_id(id_code: str):
    """Check if given ID code is valid and return the result.

    :param id_code: str
    :return: boolean
    """
    return len(id_code) == 11 and str.isnumeric(id_code) and check_gender_number(int(id_code[0]))\
        and check_year_number_two_digits(int(id_code[1:3])) and check_month_number(int(id_code[3:5]))\
        and check_day_number(get_full_year(int(id_code[0]), int(id_code[1:3])), int(id_code[3:5]), int(id_code[5:7]))\
        and check_born_order(int(id_code[7:10])) and check_control_number(id_code)


def check_gender_number(gender_number: int):
    """Check if given value is correct for gender number in ID code.

    :param gender_number: int
    :return: boolean
    """
    return gender_number in range(1, 7)


def check_year_number_two_digits(year_number: int):
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    return year_number in range(0, 100)


def check_month_number(month_number: int):
    """Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    return month_number in range(0, 13)


def check_leap_year(year_number: int):
    """Check if given year is a leap year.

    :param year_number: int
    :return: boolean
    """
    # if int(year_number) % 400 == 0:
    #     return True
    # if int(year_number) % 100 == 0:
    #     return False
    # if int(year_number) % 4 == 0:
    #     return True
    # return False
    return int(year_number) % 400 == 0 or int(year_number) % 100 != 0 and int(year_number) % 4 == 0


def check_day_number(year_number: int, month_number: int, day_number: int):
    """Check if given value is correct for day number in ID code.

    Also, consider leap year and which month has 30 or 31 days.

    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """
    return (month_number == 2
            and ((check_leap_year(year_number) and day_number in range(0, 30)) or day_number in range(0, 29))) \
        or (month_number in range(1, 8) and month_number != 2 and (month_number % 2 == 0 and day_number in range(0, 31)
            or month_number % 2 == 1 and day_number in range(0, 32))) \
        or (month_number in range(8, 13) and (month_number % 2 == 0 and day_number in range(0, 32)
            or month_number % 2 == 1 and day_number in range(0, 31)))


def check_born_order(born_order: int):
    """
    Check if given value is correct for born order number in ID code.

    :param born_order: int
    :return: boolean
    """
    return born_order in range(0, 1000)


def check_control_number(id_code: str):
    """Check if given value is correct for control number in ID code.

    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """
    numbers = [int(id_code[0]), int(id_code[1]), int(id_code[2]), int(id_code[3]), int(id_code[4]), int(id_code[5]),
               int(id_code[6]), int(id_code[7]), int(id_code[8]), int(id_code[9])]
    multip_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    multip_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    result1 = sum([numbers[i] * multip_1[i] for i in range(10)]) % 11
    if result1 == 10:
        result2 = sum([numbers[i] * multip_2[i] for i in range(10)]) % 11 % 10
        return result2 == int(id_code[10])
    return result1 == int(id_code[10])


def get_gender(gender_number: int):
    """Define the gender according to the number from ID code.

    :param gender_number: int
    :return: str
    """
    if gender_number == 1 or gender_number == 3 or gender_number == 5:
        return "male"
    elif gender_number == 2 or gender_number == 4 or gender_number == 6:
        return "female"


def get_full_year(gender_number: int, year: int):
    """Define the 4-digit year when given person was born.

    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year: int
    :return: int
    """
    if 0 < int(gender_number) < 3:
        return 1800 + int(year)
    elif 2 < int(gender_number) < 5:
        return 1900 + int(year)
    elif 4 < int(gender_number) < 7:
        return 2000 + int(year)


def get_data_from_id(id_code: str):
    """Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a (gender) born on (DD.MM.YYYY).

    :param id_code: str
    :return: str
    """
    if not check_your_id(id_code):
        return "Given invalid ID code!"
    return f"This is a {get_gender(int(id_code[0]))} born on " \
           f"{id_code[5:7]}.{id_code[3:5]}.{get_full_year(int(id_code[0]), int(id_code[1:3]))}"


if __name__ == '__main__':
    print("Overall ID check::")
    # print(check_your_id("49808270244"))  # -> True
    personal_id = input("Insert your personal ID code:")  # type your own id in command prompt
    print(check_your_id(personal_id))  # -> True
    print(get_data_from_id(personal_id))
    print(check_your_id("12345678901"))  # -> False
    print("\nGender number:")
    for i in range(9):
        print(f"{i} {check_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False
    print("\nYear number:")
    print(check_year_number_two_digits(100))  # -> False
    print(check_year_number_two_digits(50))  # -> true
    print("\nMonth number:")
    print(check_month_number(2))  # -> True
    print(check_month_number(15))  # -> False
    print("\nDay number:")
    print(check_day_number(2005, 12, 25))  # -> True
    print(check_day_number(1910, 8, 32))  # -> False
    print(check_leap_year(1804))  # -> True
    print(check_leap_year(1800))  # -> False
    print("\nFebruary check:")
    print(check_day_number(1996, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(check_day_number(2099, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(check_day_number(2008, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(check_day_number(1822, 4, 31))  # -> False (April contains max 30 days)
    print(check_day_number(2018, 10, 31))  # -> True
    print(check_day_number(1915, 9, 31))  # -> False (September contains max 30 days)
    print("\nBorn order number:")
    print(check_born_order(0))  # -> True
    print(check_born_order(850))  # -> True
    print("\nControl number:")
    print(check_control_number("49808270244"))  # -> True
    print(check_control_number("60109200187"))  # -> False, it must be 6
    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998"
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"
