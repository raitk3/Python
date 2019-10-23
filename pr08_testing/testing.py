"""Tester."""
import shortest_way_back
import random


def our_shortest_way_back(path: str) -> str:
    """Solution for tester."""
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


def generate_random_data(length, size):
    """Generate random string."""
    data = []
    for _ in range(size):
        string = "".join(random.choices("NESW", k=length))
        data.append(string)
    return data


def assert_func(string):
    """Define assert function."""
    studsol = shortest_way_back.shortest_way_back(string)
    testsol = our_shortest_way_back(string)
    assert len(testsol) == len(studsol)
    assert testsol.count("N") == studsol.count("N")
    assert testsol.count("E") == studsol.count("E")
    assert testsol.count("W") == studsol.count("W")
    assert testsol.count("S") == studsol.count("S")


def test_empty():
    """Test an empty string."""
    assert shortest_way_back.shortest_way_back("") == ""


def test_finish_at_home():
    """Test an returning string."""
    assert "" == shortest_way_back.shortest_way_back("NNSSEEWWENSWNNEESSEENNSSWWWW")


def test_simple():
    """Test multiple choice test."""
    assert shortest_way_back.shortest_way_back("NNE") in ["SSW", "SWS", "WSS"]


def test_only_n():
    """Test an only N answer."""
    assert shortest_way_back.shortest_way_back("S") == "N"


def test_only_s():
    """Test an only S answer."""
    assert shortest_way_back.shortest_way_back("N") == "S"


def test_only_w():
    """Test an only W answer."""
    assert shortest_way_back.shortest_way_back("E") == "W"


def test_only_e():
    """Test an only E answer."""
    assert shortest_way_back.shortest_way_back("W") == "E"


def test_long_answer():
    """Test a long answer."""
    string = shortest_way_back.shortest_way_back("NNNEEESNENSNENENSNENESSNNE")
    assert_func(string)


def test_random_short():
    """Test random short string."""
    data = generate_random_data(15, 20)
    for string in data:
        assert_func(string)


def test_random_long():
    """Test random log string."""
    data = generate_random_data(50, 10)
    for string in data:
        assert_func(string)


def test_random_all_chars():
    """Test all chars..."""
    string = "NANDKSFOSDKFSDKFOSDJGDOKFGSIDJHGIODKFÖHGOWRPTJPIODFJSGISHOIRWAJOEITHEOUIR"
    assert_func(string)


def test_other_letters():
    """Test anything but NEWS."""
    assert "" == shortest_way_back.shortest_way_back("QRTYUIOPADFGHJKLZXCVBM")


def test_punctuation():
    """Test punctuation marks."""
    assert "" == shortest_way_back.shortest_way_back(".,!?#%&")
