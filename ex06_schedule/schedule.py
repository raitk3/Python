"""Create schedule from the given file."""

import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    with open(input_filename) as text:
        text = text.read()
        out_text = create_schedule_string(text)

    f = open(output_filename, "w+")
    f.write(out_text)
    f.close()


def create_schedule_list(input_string):
    """Create schedule list."""
    schedule = []

    for match in re.finditer(r"\s(2[0-3]|1\d|0\d|\d)\D([0-5]\d|\d)\s+([a-zA-Z]+)", input_string):

        if len(match.group(1)) == 1:
            hours = "0" + str(match.group(1))
        else:
            hours = match.group(1)

        if len(match.group(2)) == 1:
            minutes = "0" + str(match.group(2))
        else:
            minutes = match.group(2)
        activity = match.group(3).lower()
        schedule.append(hours + ":" + minutes + "-" + activity)

    new_dict = {}
    for element in schedule:
        if element.split("-")[0] not in new_dict:
            new_dict[element.split("-")[0]] = [element.split("-")[1]]
        elif element.split("-")[1] not in new_dict[element.split("-")[0]]:
            new_dict[element.split("-")[0]].append(element.split("-")[1])
    sorted_schedule = sorted(new_dict.items(), key=(lambda x: x[0]))
    return sorted_schedule


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    sorted_schedule = create_schedule_list(input_string)
    if len(sorted_schedule) == 0:
        return "------------------\n|  time | items  |\n------------------\n| No items found |\n------------------"
    else:
        print_string = []
        time_len = 8
        activity_len = 5
        table = ""
        for el in sorted_schedule:
            activity = ", ".join(el[1])
            if len(activity) > activity_len:
                activity_len = len(activity)
        for el in sorted_schedule:
            if (el[0])[0:2] == "00":
                time = "12" + (el[0])[2:] + " AM"
                time_len = 9
            elif int((el[0])[0:2]) < 10:
                time = (el[0])[1:] + " AM"
            elif 9 < int((el[0])[0:2]) < 12:
                time = (el[0]) + " AM"
                time_len = 9
            elif 24 > (int((el[0])[0:2])) > 12:
                time = str((int((el[0])[0:2])) - 12) + (el[0])[2:] + " PM"
                time_len = 9
            else:
                time = el[0] + " PM"
                time_len = 9
            activity = ", ".join(el[1])
            print_string.append(f"|{time: >{time_len}} | {activity: <{activity_len}} |\n")
        header_string = f"{'-':->{time_len + activity_len + 6}}\n" \
                        f"|{'time': >{time_len}} | {'items': <{activity_len}} |\n" \
                        f"{'-':->{time_len + activity_len + 6}}\n"
        end_string = f"{'-':->{time_len + activity_len + 6}}"
        table += header_string
        table += "".join(print_string)
        table += end_string
        return table


if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
    print(create_schedule_string(" 1:34 aaa, 3:14 asda, 15:2 asd, 123:65 sad, 12:25 asdadasdasdasdasd"
                                 "15:44 gahjsdasdasd, 1:1 asdasd, 2:2 dafak? 0:0 nullnull, 23a59 olgu"
                                 "23f58 minu_mõistus_ei_jaga_enam, 23,58 ragequit 23257 kurat"))
    print(create_schedule_string(" 1:34 aaa, 3:14 asda, 1:2 asd, 123:65 sad, 1:25 asdadasdasdasdasd"
                                 "9:44 gahjsdasdasd, 1:1 asdasd, 2:2 dafak? 3:0 nullnull, 4a59 olgu"
                                 "7f58 minu_mõistus_ei_jaga_enam, 6,58 ragequit 23257 kurat"))
    print(create_schedule_string(""))
    print(create_schedule_string("n 1:1 kllpojkpkoijiuhkjbluygluiholuhlij 7o5 ujhi"))
