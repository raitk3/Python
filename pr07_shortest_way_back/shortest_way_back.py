"""Find the shortest way back in a taxicab geometry."""


def shortest_way_back(path: str) -> str:
    """
    Find the shortest way back in a taxicab geometry.

    :param path: string of moves, where moves are encoded as follows:.
    N - north -  (1, 0)
    S - south -  (-1, 0)
    E - east  -  (0, 1)
    W - west  -  (0, -1)
    (first coordinate indicates steps towards north,
    second coordinate indicates steps towards east)

    :return: the shortest way back encoded the same way as :param path:.
    """
    x, y = 0, 0
    compass = {"N": (1, 0),
               "S": (-1, 0),
               "E": (0, 1),
               "W": (0, -1)
               }
    for el in path:
        if el in compass:
            x += compass[el][0]
            y += compass[el][1]
    directions = ""
    if x > 0:
        directions += x * "S"
    if x < 0:
        directions += -x * "N"
    if y > 0:
        directions += y * "W"
    if y < 0:
        directions += -y * "E"
    return directions


if __name__ == '__main__':
    assert shortest_way_back("NNN") == "SSS"
    assert shortest_way_back("SS") == "NN"
    assert shortest_way_back("E") == "W"
    assert shortest_way_back("WWWW") == "EEEE"

    assert shortest_way_back("") == ""
    assert shortest_way_back("NESW") == ""

    assert shortest_way_back("NNEESEW") in ["SWW", "WSW", "WWS"]
