import re


def func(input_list, keyword):
    count = 0
    for el in input_list:
     count += len(re.findall(keyword, el.lower()))
    return count
# def func(input_string, keyword):
#     counter = 0
#     for match in re.finditer(keyword, input_string.lower()):
#         counter += 1
#     return counter


if __name__ == '__main__':
    print(func(["Anna", "anna ANNA ei Anna..."], "anna"))