"""Hobbies."""
import csv


def create_list_from_file(file):
    """
    Collect lines from given file into list.

    :param file: original file path
    :return: list of lines
    """
    with open(file) as list1:
        collected_data = list1.read().splitlines()
        return collected_data


def create_dictionary(file):
    """
    Create dictionary about given peoples' hobbies as Name: [hobby_1, hobby_2].

    :param file: original file path
    :return: dict
    """
    list1 = create_list_from_file(file)
    new_dict = {}
    for element in list1:
        if element.split(":")[0] not in new_dict:
            new_dict[element.split(":")[0]] = [element.split(":")[1]]
        elif element.split(":")[1] not in new_dict[element.split(":")[0]]:
            new_dict[element.split(":")[0]].append(element.split(":")[1])
    return new_dict


def find_person_with_most_hobbies(file):
    """
    Find the person (or people) who have more hobbies than others.

    :param file: original file path
    :return: list
    """
    dic = create_dictionary(file)
    max_len = 0
    max_key = []
    for key in dic:
        if len(dic[key]) > max_len:
            max_key = [key]
            max_len = len(dic[key])
        elif len(dic[key]) == max_len:
            max_key.append(key)
    return max_key


def find_person_with_least_hobbies(file):
    """
    Find the person (or people) who have less hobbies than others.

    :param file: original file path
    :return: list
    """
    dic = create_dictionary(file)
    min_len = -1
    min_key = []
    for key in dic:
        if min_len == -1 or len(dic[key]) < min_len:
            min_key = [key]
            min_len = len(dic[key])
        elif len(dic[key]) == min_len:
            min_key.append(key)
    return min_key


def create_hobbies_list(file):
    """Create hobbies list."""
    hobbies = create_list_from_file(file)
    new_dict = {}
    for element in hobbies:
        if element.split(":")[1] not in new_dict:
            new_dict[element.split(":")[1]] = 1
        elif element.split(":")[1] in new_dict:
            new_dict[element.split(":")[1]] += 1
    return new_dict


def find_most_popular_hobby(file):
    """
    Find the most popular hobby.

    :param file: original file path
    :return: list
    """
    hobbies = create_hobbies_list(file)
    new_list = []
    max_number = 0

    for key in hobbies:
        if hobbies[key] > max_number:
            new_list = [key]
            max_number = hobbies[key]
        elif hobbies[key] == max_number:
            new_list.append(key)
    return new_list


def find_least_popular_hobby(file):
    """
    Find the least popular hobby.

    :param file: original file path
    :return: list
    """
    hobbies = create_hobbies_list(file)
    new_list = []
    min_number = -1

    for key in hobbies:
        if min_number == -1 or hobbies[key] < min_number:
            new_list = [key]
            min_number = hobbies[key]
        elif hobbies[key] == min_number:
            new_list.append(key)
    return new_list


def write_corrected_database(file, file_to_write):
    """
    Write .csv file in a proper way. Use collected and structured data.

    :param file: original file path
    :param file_to_write: file to write result
    """
    with open(file_to_write, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        name = "Name"
        hobbies = "Hobbies"
        writer.writerow([name, hobbies])
        # your code goes here
        dict2 = create_dictionary(file)
        new_list = []
        for key in dict2:
            name = key
            hobbies = sorted(dict2[key])
            hobbies = "-".join(hobbies)
            new_list.append(name + "," + hobbies)
        new_list = sorted(new_list)
        print(new_list)
        for el in new_list:
            writer.writerows([[el]])

# These examples are based on a given text file from the exercise.


if __name__ == '__main__':
    dict = create_dictionary("hobbies_database.txt")
    print(len(create_list_from_file("hobbies_database.txt")))  # -> 100
    print("Check presence of hobbies for chosen person:")
    print("shopping" in dict["Wendy"])  # -> True
    print("fitness" in dict["Sophie"])  # -> False
    print("gaming" in dict["Peter"])  # -> True
    print("Check if hobbies - person relation is correct:")
    print("Check if a person(people) with the biggest amount of hobbies is(are) correct:")
    print(find_person_with_most_hobbies("hobbies_database.txt"))  # -> ['Jack']
    print(len(dict["Jack"]))  # ->  12
    print(len(dict["Carmen"]))  # -> 10
    print("Check if a person(people) with the smallest amount of hobbies is(are) correct:")
    print(find_person_with_least_hobbies("hobbies_database.txt"))  # -> ['Molly']
    print(len(dict["Molly"]))  # -> 5
    print(len(dict["Sophie"]))  # -> 7
    print("Check if the most popular hobby(ies) is(are) correct")
    print(find_most_popular_hobby("hobbies_database.txt"))  # -> ['theatre', 'gaming', 'driving']
    print("Check if the least popular hobby(ies) is(are) correct")
    print(find_least_popular_hobby("hobbies_database.txt"))  # -> ['dance', 'puzzles', 'flowers']
    write_corrected_database("hobbies_database.txt", 'correct_hobbies_database.csv')
