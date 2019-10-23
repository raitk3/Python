import re


class Star:
    """Star itself."""

    def __init__(self, name, x, y, move_x, move_y):
        self.name = name
        self.x = y
        self.y = x
        self.move_x = move_y
        self.move_y = move_x

    def move_star(self):
        self.x += self.move_x
        self.y += self.move_y

    def __repr__(self):
        return f"({self.name}, {self.x}, {self.y})"


if __name__ == '__main__':
    stars = []
    data = """-917 1837 1 -2
    -916 -1835 1 2
    -915 2755 1 -3
    -1832 -1835 2 2
    3677 2755 -4 -3
    -2748 2755 3 -3
    -909 -917 1 1
    3696 2755 -4 -3
    -3643 -4589 4 5
    -886 4591 1 -5
    -3635 -917 4 1
    -4550 2755 5 -3
    959 3673 -1 -4
    960 -917 -1 1
    -3629 1837 4 -2
    -4546 4591 5 -5
    -3624 919 4 -1
    -3623 1837 4 -2
    -2704 4591 3 -5
    969 919 -1 -1
    1888 -1835 -2 2
    -3671 4592 4 -5
    -1827 2756 2 -3
    3696 -3670 -4 4
    2779 -3670 -3 4
    4618 4592 -5 -5
    -3643 -4588 4 5
    950 3674 -1 -4
    1873 920 -2 -1
    -2714 -4588 3 5
    -2709 -916 3 1
    3720 2756 -4 -3
    1889 2756 -2 -3
    -917 -4587 1 5
    927 1839 -1 -2
    1860 2757 -2 -3
    4615 2757 -5 -3
    -1808 -3669 2 4
    4619 -2751 -5 3
    950 -915 -1 1
    3709 -2751 -4 3
    1876 -3669 -2 4
    1881 921 -2 -1
    -4542 1839 5 -2
    -4537 -4587 5 5
    2755 2758 -3 -3
    4599 3676 -5 -4
    4614 -4586 -5 5
    -4564 -3668 5 4
    4617 -2750 -5 3
    2783 -1832 -3 2
    3704 4594 -4 -5
    -1799 -3668 2 4
    -1796 4594 2 -5
    -4545 3676 5 -4
    -1788 3676 2 -4
    -2701 -1832 3 2
    -1835 -3667 2 4
    2756 -2749 -3 3
    -3669 923 4 -1
    -4586 3677 5 -4
    -3667 -2749 4 3
    1845 -1831 -2 2
    -3662 1841 4 -2
    -2743 -1831 3 2
    -4578 1841 5 -2
    -4577 -4585 5 5
    -3655 3677 4 -4
    1857 4595 -2 -5
    942 2759 -1 -3
    4616 4595 -5 -5
    -4563 2759 5 -3
    947 2759 -1 -3
    -2722 2759 3 -3
    -881 -4585 1 5
    -878 -4585 1 5
    1877 -1831 -2 2
    -3630 -3667 4 4
    -875 -2749 1 3
    3716 -4585 -4 5
    4638 -913 -5 1
    -2705 -913 3 1
    3722 3677 -4 -4
    3723 2759 -4 -3
    -866 2759 1 -3
    919 -912 -1 1
    2763 924 -3 -1
    -904 924 1 -1
    935 -1830 -1 2
    -897 -2748 1 3
    -4566 4596 5 -5
    -889 -4584 1 5
    -2722 2760 3 -3
    4627 -2748 -5 3
    2794 4596 -3 -5
    963 -912 -1 1
    -870 -1830 1 2
    -2705 4596 3 -5
    -4589 925 5 -1
    -909 -1829 1 2
    -1822 -911 2 1
    -2737 -911 3 1
    -897 2761 1 -3
    2778 4597 -3 -5
    3701 -911 -4 1
    950 -1829 -1 2
    -881 -4583 1 5
    4630 -1829 -5 2
    2799 2761 -3 -3
    -870 3679 1 -4
    -4540 2761 5 -3
    2755 -910 -3 1
    -1827 4598 2 -5
    4604 926 -5 -1
    4608 3680 -5 -4
    3692 3680 -4 -4
    1860 -910 -2 1
    2783 1844 -3 -2
    -3640 3680 4 -4
    4627 4598 -5 -5
    -4550 2762 5 -3
    4635 -3664 -5 4
    2802 1844 -3 -2
    3723 -2746 -4 3
    -2753 927 3 -1
    -4581 927 5 -1
    2768 -909 -3 1
    2772 -4581 -3 5
    3692 1845 -4 -2
    -1812 -4581 2 5
    -1807 -1827 2 2
    -2722 -3663 3 4
    955 4599 -1 -5
    958 -4581 -1 5
    -3627 3681 4 -4
    -3624 1845 4 -2
    970 927 -1 -1
    4591 928 -5 -1
    -4580 -908 5 1
    2765 1846 -3 -2
    4602 -3662 -5 4
    4603 -1826 -5 2
    -2735 4600 3 -5
    1860 928 -2 -1
    -2725 -1826 3 2
    4623 -4580 -5 5
    3706 3682 -4 -4
    4625 -1826 -5 2
    -4554 -3662 5 4
    -3632 -3662 4 4
    -2713 928 3 -1
    2796 -3662 -3 4
    1879 1846 -2 -2
    -4546 2764 5 -3
    -1788 -3662 2 4
    -4537 -908 5 1"""
    name = 1
    for match in re.finditer(r"(-*\d+) (-*\d+) (-*\d+) (-*\d+)", data):
        stars.append(Star(str(name), int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))))
        name += 1
    print(stars)
    for _ in range(918):
        for el in stars:
            el.move_star()
    print(stars)
    map = []
    for i in range(20):
        map.append("░" * 60)
    for star in stars:
        map[star.x] = map[star.x][0:star.y] + "▓" + map[star.x][star.y + 1:]
    for el in map:
        print(el + "\n")
