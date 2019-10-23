def is_prime_number(number):
    if number < 2:
        return False
    elif number < 4 and number != 1:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
    return True


if __name__ == '__main__':
    while True:
        print(is_prime_number(int(input())))
