"""Polar and cartesian points converter."""

from math import degrees, radians, pi, sin, cos, sqrt, atan
"""Import only necessary stuff..."""


def convert_polar_to_cartesian(r, phi):
    """Polar to cartesian..."""
    rad = radians(phi)
    while rad <= (-180):
        rad = rad + 360
    while rad > 180:
        rad = rad - 360
    """These are because angle should be between (-180;180]"""
    x = (r * (cos(rad)))
    y = (r * (sin(rad)))
    x = round(x, 2)
    y = round(y, 2)
    return x, y


def arctan2(x, y):
    """Define arcustangens function."""
    arctan = atan(y / x)
    return arctan


def convert_cartesian_to_polar(x, y):
    """Cartesian to polar..."""
    r = sqrt(x**2 + y**2)
    r = round(r, 2)
    if x > 0:
        rad = (arctan2(x, y))
    elif x < 0 <= y:
        rad = (arctan2(x, y) + pi)
    elif x < 0 and y < 0:
        rad = (arctan2(x, y) - pi)
    elif x == 0 and y > 0:
        rad = (pi / 2)
    elif x == 0 and y < 0:
        rad = (-pi / 2)
    else:
        rad = 0
    deg = degrees(rad)
    deg = round(deg, 2)
    return r, deg


if __name__ == '__main__':
    """Just for check."""
    print("to polar")
    print(convert_cartesian_to_polar(1, 1))  # (1.41, 45.0)
    print(convert_cartesian_to_polar(0, 0))  # (0.0, 0.0)
    print(convert_cartesian_to_polar(0, 1))  # (1.0, 90.0)
    print(convert_cartesian_to_polar(-3, -4))  # (5.0, -126.87)

    print("to cartesian")
    print(convert_polar_to_cartesian(1, 90))  # (0.0, 1.0)
    print(convert_polar_to_cartesian(0, 0))  # (0.0, 0.0)
    print(convert_polar_to_cartesian(2, 60))  # (1.0, 1.73)
    print(convert_polar_to_cartesian(3, -40))  # (2.3, -1.93)
