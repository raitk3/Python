"""Ponies."""
import base64
import re


def read(file):
    """Read info from file."""
    try:
        ponies_list = []
        with open(file) as text:
            for line in text:
                line = decode(line)
                if extract_information(line) != {}:
                    ponies_list.append(extract_information(line))
        return ponies_list
    except FileNotFoundError:
        raise Exception("File not found!")


def decode(line: str) -> str:
    """Decode base64 to UTF-8."""
    return base64.b64decode(line).decode('UTF-8')


def extract_information(text):
    """Extract info from text."""
    new_dict = {}
    for match in re.finditer(r"([A-Z][a-z]+ [A-Z][a-z]+) +(\w+) +(\w+) +(\w+) +(\w+) +(\w+ *\w* *\w*)", text):
        new_dict["name"] = match.group(1)
        new_dict["kind"] = match.group(2)
        new_dict["coat_color"] = match.group(3)
        new_dict["mane_color"] = match.group(4)
        new_dict["eye_color"] = match.group(5)
        new_dict["location"] = match.group(6)
    return new_dict


def filter_by_location(ponies: list) -> list:
    """Filter ponies by location."""
    filtered_ponies = []
    for pony in ponies:
        if pony["location"] != "None":
            filtered_ponies.append(pony)
    return filtered_ponies


def filter_by_kind(ponies: list, kind: str) -> list:
    """Filter ponies by kind."""
    filtered_ponies = []
    for pony in ponies:
        if pony["kind"] == kind:
            filtered_ponies.append(pony)
    return filtered_ponies


def get_points_for_color(color: str):
    """Give colors values."""
    colors = [
        'magenta', 'pink', 'purple', 'orange', 'red', 'yellow', 'cyan', 'blue', 'brown', 'green'
    ]
    color_dict = {}
    max_points = 10
    for el in colors:
        color_dict[el] = max_points
        max_points += -1
    if color in colors:
        awarded_points = color_dict[color]
        if awarded_points < 5:
            return
        else:
            return awarded_points


def add_points(pony: dict) -> dict:
    """Give ponies their points."""
    evaluation_locations = {
        'coat_color': ['Town Hall', 'Theater', 'School of Friendship'],
        'mane_color': ['Schoolhouse', 'Crusaders Clubhouse', 'Golden Oak Library'],
        'eye_color': ['Train station', 'Castle of Friendship', 'Retirement Village']
    }
    attribute = ""
    for el in evaluation_locations:
        if pony["location"] in evaluation_locations[el]:
            attribute = el

    if attribute != "":
        color = pony[attribute]
        pony["points"] = get_points_for_color(color)
    return pony


def evaluate_ponies(ponies: list) -> list:
    """Evaluate ponies."""
    evaluated_ponies = []
    for pony in ponies:
        evaluated_ponies.append(add_points(pony))
    return evaluated_ponies


def sort_by_name(ponies: list) -> list:
    """Sort ponies by name."""
    return sorted(ponies, key=lambda x: x["name"])


def sort_by_points(ponies: list) -> list:
    """Sort ponies by points."""
    ponies_without_none = []
    for pony in ponies:
        if pony["points"] is not None:
            ponies_without_none.append(pony)
    return sorted(ponies_without_none, key=lambda x: x["points"], reverse=True)


def format_line(pony: dict, place: int) -> str:
    """Format line for text."""
    return f"{place: <10}{pony['points']: <10}{pony['name']: <20}{pony['kind']: <20}{pony['coat_color']: <20}" \
           f"{pony['mane_color']: <20}{pony['eye_color']: <20}{pony['location']}"


def write(input_file: str, kind: str):
    """Write table as text."""
    place = 1
    ponies = read(input_file)
    ponies_filtered = filter_by_kind(filter_by_location(ponies), kind)
    ponies_evaluated = evaluate_ponies(ponies_filtered)
    ponies_sorted = sort_by_points(sort_by_name(ponies_evaluated))

    header_string = f"{'PLACE': <10}{'POINTS': <10}{'NAME': <20}{'KIND': <20}{'COAT COLOR': <20}{'MANE COLOR': <20}" \
                    f"{'EYE COLOR': <20}LOCATION\n{'':-<128}\n"  # Header
    file_name = "results_for_" + kind + ".txt"
    output_file = open(file_name, "w")
    output_file.write(header_string)
    printable_strings = []
    for pony in ponies_sorted:
        printable_strings.append(format_line(pony, place))
        place += 1
    output_file.write("\n".join(printable_strings))


if __name__ == '__main__':
    """
    print(decode("TWF1ZCBQb21tZWwgICAgICAgICBVbmljb3JuICAgICAgICAgICAgIHBpbmsgICAgICAgICAgICAgICAgZ3JlZW4gICAgICAgICAgICAgICBjeWFuICAgICAgICAgICAgICAgIENhc3RsZSBvZiBGcmllbmRzaGlw"))
    print(extract_information("TWF1ZCBQb21tZWwgICAgICAgICBVbmljb3JuICAgICAgICAgICAgIHBpbmsgICAgICAgICAgICAgICAgZ3JlZW4gICAgICAgICAgICAgICBjeWFuICAgICAgICAgICAgICAgIENhc3RsZSBvZiBGcmllbmRzaGlw"))
    print(sort_by_name(read("näidis_sisendfail.txt")))"""
    write("näidis_sisendfail.txt", "Pegasus")
    write("näidis_sisendfail.txt", "Unicorn")
    write("näidis_sisendfail.txt", "Alicorn")
    write("näidis_sisendfail.txt", "Earth")
