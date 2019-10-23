"""Simulation."""
from typing import Tuple


def simulate(world_map: list, flight_plan: list) -> list:
    """
    Simulate a flying space ship fighting space pirates.

    :param world_map: A list of strings indicating rows that make up the space map.
                 The space map is always rectangular and the minimum given size is 1x1.
                 Space pirate free zone is indicated by the symbol ('-'), low presence by ('w') and high presence by ('W').
                 The ship position is indicated by the symbol ('X'). There is always one ship on the space map.
                 Asteroid fields are indicated by the symbol ('#').

    :param flight_plan: A list of moves.
                  The moves are abbreviated N - north, E - east, S - south, W - west.
                  Ignore moves that would put the ship out of bounds or crash it into an asteroid field.

    :return: A list of strings indicating rows that make up the space map. Same format as the given wmap.

    Pirates under Shippy's starting position are always eliminated ('-').
    If Shippy fights pirates in high presence area, it first turns into low presence ('w')
     and then from low presence into no presence area ('-').
    """
    width = 0
    height = 0
    dmap, x, y = list_to_dictionary_converter(world_map)
    directions = {
        "N": (-1, 0),
        "S": (1, 0),
        "E": (0, 1),
        "W": (0, -1)
    }

    for direction in flight_plan:
        x_temp = x + directions[direction][0]
        y_temp = y + directions[direction][1]
        if (x_temp, y_temp) in dmap:
            if dmap[x_temp, y_temp] != "#":
                if dmap[x_temp, y_temp] == "W":
                    dmap[x_temp, y_temp] = "w"
                    x, y = x_temp, y_temp
                else:
                    x, y = x_temp, y_temp
                    dmap[x, y] = "-"
    dmap[x, y] = "X"
    for el in dmap:
        x, y = el
        if x >= height:
            height = x + 1
        if y >= width:
            width = y + 1
    new_map = dictionary_to_list_converter(dmap, width, height)
    return new_map


def list_to_dictionary_converter(world_map: list) -> Tuple[dict, int, int]:
    """
    Convert a list to dictionary using coordinates as keys.

    :param world_map: list of strings.
    :return: dictionary of the space, shippy y position, shippy x position

    Map tile under Shippy's location is marked as "-" or no presence area.
    Dictionaries key is a Tuple which has Y-position as the first value and X-position as
    the second value. If there is no Shippy (Marked as X in the list) in the list, the
    coordinates are marked as 0 and 0.
    """
    dmap = {}
    x = 0
    y = 0
    for rowi, row in enumerate(world_map):
        for coli, col in enumerate(row):
            if row[coli] == "X" or row[coli] == "x":
                x = rowi
                y = coli
                dmap[rowi, coli] = "-"
            else:
                dmap[rowi, coli] = row[coli]
    return dmap, x, y


def dictionary_to_list_converter(space_map: dict, width: int, height: int) -> list:
    """
    Convert dictionary of coordinates to list of strings.

    :param space_map: Dictionary of the space
    :param width: Width of the world.
    :param height: Height of the world.
    :return: List of strings

    PS: You should add Shippy back the the dictionary before you call this method.
    """
    new_map = []
    blank_string = f"{'-':-<{width}}"
    for i in range(0, height):
        new_map.append(blank_string)
    for el in space_map:
        x, y = el
        new_map[x] = new_map[x][:y] + space_map[el] + new_map[x][y + 1:]
    return new_map


if __name__ == '__main__':

    space_list1 = [
        "#www-",
        "wXw#-",
    ]
    flight_plan1 = ["N", "E", "E", "S", "E"]
    print("\n".join(simulate(space_list1, flight_plan1)))
    print(list_to_dictionary_converter(flight_plan1))

    # #---X
    # w-w#-

    print(simulate(space_list1, flight_plan1))  # == ["#---X", "w-w#-"]

    print()

    space_list2 = [
        "WWWW",
        "-wwW",
        "X-#W",
    ]

    flight_plan2 = ["N", "N", "E", "E", "S", "W", "W", "S", "E", "E"]
    print("\n".join(simulate(space_list2, flight_plan2)))

    # wwwW
    # ---W
    # -X#W

    print(simulate(space_list2, flight_plan2))
    assert simulate(space_list2, flight_plan2) == ["wwwW", "---W", "-X#W"]

    assert list_to_dictionary_converter(["-"]) == ({(0, 0): "-"}, 0, 0)
    assert list_to_dictionary_converter(['W#', '-X']) == ({(0, 0): 'W', (0, 1): '#', (1, 0): '-', (1, 1): '-'}, 1, 1)

    assert list_to_dictionary_converter(
        world_map=space_list1
    ) == ({(0, 0): '#', (0, 1): 'w', (0, 2): 'w', (0, 3): 'w', (0, 4): '-', (1, 0): 'w', (1, 1): '-', (1, 2): 'w',
           (1, 3): '#', (1, 4): '-'}, 1, 1)

    assert dictionary_to_list_converter(
        {(0, 0): '#', (0, 1): 'w', (0, 2): 'w', (0, 3): 'w', (0, 4): '-', (1, 0): 'w', (1, 1): 'X', (1, 2): 'w',
         (1, 3): '#', (1, 4): '-'}, 5, 2) == space_list1

    assert dictionary_to_list_converter({(0, 0): "X"}, 1, 1) == ["X"]
