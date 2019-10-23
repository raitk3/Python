"""PR15 Statistics - lambdas."""


class Person:
    """Represent a person."""

    def __init__(self, first_name, last_name, email, gender, age):
        """Init..."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.age = age

    def __repr__(self):
        """Repr..."""
        return self.first_name


def get_oldest_person(person_list):
    """
    Return the person with the highest age.

    If multiple people are of the given age, return the first in the list.

    :param person_list: input list
    :return: Person object
    """
    return [person for person in person_list if person.age == max(person.age for person in person_list)][0]


def get_person_with_shortest_name(person_list):
    """
    Return the person with the shortest name (first name + last name).

    If there are multiple, return the first in the list.

    :param person_list:
    :return:
    """
    return min(person_list, key=lambda x: len(x.first_name + x.last_name))


def get_all_underage_people(person_list):
    """
    Return a list of all underage (under 18) people in the given list.

    :param person_list: input list of Person objects
    :return: list of all underage people
    """
    return [person for person in person_list if person.age < 18]


def filter_list_by_gender(person_list, gender):
    """
    Filter the given list by the given gender.

    :param person_list: input list of Person objects
    :param gender: string 'Male' or 'Female'
    :return: a list of persons with the given gender
    """
    return list(filter(lambda person: person.gender == gender, person_list))


def get_people_with_government_emails(person_list):
    """
    Return a list of all people with an email ending with '.gov'.

    :param person_list: input list
    :return: a list of Person objects with an government email.
    """
    return list(filter(lambda person: person.email[-4:] == ".gov", person_list))


def sort_list_by_email_length(person_list):
    """
    Sort the given list by the length of a persons email in ascending order.

    :param person_list: input list
    :return: a sorted list of Person objects
    """
    return list(sorted(person_list, key=lambda person: len(person.email)))


def get_list_of_all_names_in_uppercase(person_list):
    """
    Return a list of the first names of all persons in the list, in uppercase.

    :param person_list: input list
    :return: a list of uppercase first names
    """
    return list(map(lambda x: x.first_name.upper(), person_list))


if __name__ == "__main__":
    jack = Person("Jack", "O'Neill", "jack@sgone.com", "Male", 50)
    sam = Person("Samantha", "Carter", "sam@sgone.com", "Female", 41)
    hammond = Person("George", "Hammond", "george.hammond@usaf.gov", "Male", 65)
    ryac = Person("Rya'c", "Teal'cson", "ryac@chulak.sg", "Male", 12)
    cassie = Person("Cassandra", "Fraiser", "cassandra@gmail.sg", "Female", 16)

    person_list = [jack, sam, hammond, ryac, cassie]

    print(get_oldest_person(person_list))  # hammond
    print(get_person_with_shortest_name(person_list))  # jack
    print(get_all_underage_people(person_list))  # [ryac, cassie]
    print(filter_list_by_gender(person_list, "Female"))  # [sam, cassie]
    print(get_people_with_government_emails(person_list))  # [hammond]
    print(sort_list_by_email_length(person_list))  # [sam, jack, ryac, cassie, hammond]
    print(get_list_of_all_names_in_uppercase(person_list))  # ["JACK", "SAMANTHA", ...]
