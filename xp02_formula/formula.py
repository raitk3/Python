import re

regex_a = r"(-* *\d*)x2(?=\s)"
regex_b = r"(-* *\d*)x1*(?!\d)"
regex_c = r"(?<=\s)(-* *\d+)(?!x)"


def get_sum(list):
    """Pretty mutch sum it up."""
    sum = 0
    reverse = False
    for el in list:
        if el == "=":
            if sum > 0:
                reverse = True
            elif sum == 0:
                pass
        elif el == "":
            if reverse:
                sum -= 1
            else:
                sum += 1
        elif el == "-":
            if reverse:
                sum += 1
            else:
                sum -= 1
        else:
            if reverse:
                sum -= int(el)
            else:
                sum += int(el)
    if sum > 0:
        return f"+ {sum}"
    if sum < 0:
        return str(sum).replace("-", "- ")
    else:
        return str(sum)


def normalize_equation(equation):
    x2_multipliers = get_sum([str(match.group(1)).replace(" ", "") for match in re.finditer(regex_a, equation)])
    if x2_multipliers == "0":
        x2_multipliers = ""
    else:
        if x2_multipliers in ["-1", "1"]:
            x2_multipliers = x2_multipliers.replace("1", "")
        x2_multipliers = x2_multipliers + "x2 "
    x_multipliers = get_sum([str(match.group(1)).replace(" ", "") for match in re.finditer(regex_b, equation)])
    if x_multipliers == "0":
        x_multipliers = ""
    else:
        x_multipliers = x_multipliers + "x "
    c_multipliers = get_sum([str(match.group(1)).replace(" ", "") for match in re.finditer(regex_c, equation)])
    if c_multipliers == "0":
        c_multipliers = ""
    else:
        c_multipliers = c_multipliers + " "
    return f"{x2_multipliers}{x_multipliers}{c_multipliers}= 0".strip("+ ")


if __name__ == '__main__':
    print(normalize_equation("x2 + 2x = 3"))  # = > "x2 + 2x - 3 = 0"
    print(normalize_equation("0 = 3 + 1x2"))  # = > "x2 + 3 = 0"
    print(normalize_equation("2x + 2 = 2x2"))  # = > "2x2 - 2x - 2 = 0"
    print(normalize_equation("0x2 - 2x = 1"))  # = > "2x + 1 = 0"
    print(normalize_equation("0x2 - 2x = 1"))  # = > "2x + 1 = 0"
    print(normalize_equation("2x2 + 3x - 4 + 0x2 - x1 + 0x1 + 12 - 12x2 = 4x2 + x1 - 2"))  # = > "14x2 - x - 10 = 0"
