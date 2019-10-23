"""Rabbit_test."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """Let s see..."""
    t = 0
    prev_diff = 0

    buffer = []
    if jump_distance1 > jump_distance2:
        while pos1 != pos2:
            if jump_or_not_to_jump(t, sleep1):
                pos1 += jump_distance1
            if jump_or_not_to_jump(t, sleep2):
                pos2 += jump_distance2
            if pos1 < pos2 or pos1 > pos2 and sleep2 < sleep1:
                if t == 0:
                    prev_diff = pos1 - pos2
                    buffer = [prev_diff]
                else:
                    diff = pos1 - pos2
                    if diff > prev_diff and jump_distance1 / sleep1 > jump_distance2 / sleep2 and diff > jump_distance2:
                        return -1
                    if len(buffer) < max([sleep1, sleep2]) + 1:
                        buffer.append(diff)
                    if len(buffer) == max([sleep1, sleep2]) + 1:
                        if buffer[0] == buffer[-1]:
                            return -1
                    prev_diff = diff
            t += 1
        return pos1
    elif jump_distance2 > jump_distance1:
        return meet_me(pos2, jump_distance2, sleep2, pos1, jump_distance1, sleep1)
    elif jump_distance1 == jump_distance2 and pos1 != pos2:
        return -1


def jump_or_not_to_jump(time, sleep):
    return time % sleep == 0


if __name__ == '__main__':

    print(meet_me(1, 2, 1, 2, 1, 1))
    print(meet_me(1, 2, 3, 4, 5, 5))
    print(meet_me(10, 7, 7, 5, 8, 6))
    print(meet_me(100, 7, 4, 300, 8, 6))
    print(meet_me(1, 7, 1, 15, 5, 1))
    print(meet_me(0, 1, 1, 1, 1, 1))
