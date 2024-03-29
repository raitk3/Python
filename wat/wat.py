"""Say wat."""
import math
first_count = -1


def first(n: int):
    """
    Some 1st wat.

    So...input n seems irrelevant, only need to count, how many times this function has been called out and...that's it?
    At first 2*0, then 2*1 etc.
    """
    global first_count
    if first_count == 4:
        first_count += 1
        return 11
    else:
        first_count += 1
        return 2 * first_count


def last_neg(n):
    """helping."""
    if n > -15:
        return 0
    elif n > -625:
        return 19 * n + 501
    elif n > -1624:
        return 2 * n + 1901
    elif n > -7020:
        if n % 2 == 0:
            return n / 2
        elif n % 2 == 1:
            return n / 2 + 3
    else:
        return round(n / 3 + 3000 + (2 / 3), 0)


def last_pos(n):
    """helpints."""
    if n < 103:
        return n * 2 + 6
    elif n < 999:
        return int(n * 0.5) - 769 + (n % 137) - 1
    elif n < 1012:
        return chr(2 * n - 1900)
    elif n < 2003:
        return int(math.sqrt(n))
    elif n < 7982:
        return n - (n // 1337) * 1337
    else:
        return sum(int(number) for number in str(n)) + 1


def last(n: int):
    """last with some help..."""
    if n >= -3:
        return last_pos(n)
    else:
        return last_neg(n)


if __name__ == '__main__':
    correct_answer = {
        -11528: -842,
        -11459: -819,
        -11340: -779,
        -10618: -539,
        -9634: -211,
        -9350: -116,
        -8815: 62,
        -8585: 139,
        -7398: 535,
        -6838: -3419,
        -6797: -3395.5,
        -6498: -3249,
        -6246: -3123,
        -3701: -1847.5,
        -3507: -1750.5,
        -3164: -1582,
        -3073: -1533.5,
        -2901: -1447.5,
        -2393: -1193.5,
        -2286: -1143,
        -1878: -939,
        -1815: -904.5,
        -1774: -887,
        -1764: -882,
        -707: 487,
        -765: 371,
        -1231: -561,
        -1388: -875,
        -590: -10709,
        -568: -10291,
        -564: -10215,
        -563: -10196,
        -552: -9987,
        -540: -9759,
        -503: -9056,
        -480: -8619,
        -470: -8429,
        -444: -7935,
        -441: -7878,
        -423: -7536,
        -400: -7099,
        -382: -6757,
        -374: -6605,
        -365: -6434,
        -353: -6206,
        -341: -5978,
        -329: -5750,
        -296: -5123,
        -291: -5028,
        -279: -4800,
        -273: -4686,
        -271: -4648,
        -255: -4344,
        -213: -3546,
        -189: -3090,
        -176: -2843,
        -174: -2805,
        -165: -2634,
        -137: -2102,
        -85: -1114,
        -65: -734,
        -40: -259,
        -22: 83,
        -11: 0,
        -10: 0,
        -7: 0,
        0: 6,
        2: 10,
        7: 20,
        23: 52,
        39: 84,
        44: 94,
        48: 102,
        63: 132,
        71: 148,
        73: 152,
        83: 172,
        89: 184,
        92: 190,
        93: 192,
        94: 194,
        99: 204,
        100: 206,
        102: 210,
        115: -598,
        136: -566,
        138: -700,
        147: -687,
        237: -552,
        265: -510,
        275: -632,
        317: -569,
        342: -531,
        408: -432,
        414: -560,
        437: -526,
        498: -434,
        512: -413,
        521: -400,
        542: -368,
        565: -471,
        594: -427,
        613: -399,
        682: -295,
        679: -300,
        708: -393,
        786: -276,
        820: -225,
        833: -343,
        843: -328,
        869: -289,
        922: -209,
        993: -240,
        998: -232,
        999: "b",
        1000: "d",
        1001: "f",
        1002: "h",
        1003: "j",
        1004: "l",
        1005: "n",
        1006: "p",
        1007: "r",
        1008: "t",
        1009: "v",
        1010: "x",
        1011: "z",
        1296: 36,
        1725: 41,
        1786: 42,
        10270: 11,
        10760: 15,
        10765: 20,
        8784: 28,
        8024: 15,
        11586: 22,
        8206: 17,
        9618: 25,
        9347: 24,
        10064: 12,
        8495: 27,
        11217: 13,
        -747: 407,
        -770: 361,
        -1175: -449,
        -287: -4952,
        -22: 83,
        -408: -7251,
        6923: 238,
        4507: 496,
        4392: 381,
        10342: 11,
        10209: 13,
        8878: 32,
        1224: 34,
        2132: 795,
        7986: 31
    }
    wrong_list = []
    for element in correct_answer:
        if last(element) != correct_answer[element]:
            wrong_list.append(element)
            print(element)
