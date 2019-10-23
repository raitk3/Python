"""Encode and decode Caesar cipher."""
import string


def encode(message: str, shift: int, alphabet=string.ascii_lowercase) -> str:
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    new_message = ""  # Create a new string, where I create the encoded message.
    for letter in message:
        if letter in alphabet:
            letter = alphabet[(alphabet.find(letter) + shift) % len(alphabet)]
        elif letter.isupper:
            letter_lower = letter.lower()
            if letter_lower in alphabet:
                letter = alphabet[(alphabet.find(letter_lower) + shift) % len(alphabet)]
                letter = letter.upper()
        new_message = new_message + letter  # Creates the new message.
    return new_message


def decode(message: str, shift: int, alphabet=string.ascii_lowercase) -> str:
    """
    Decode the given message already encoded with the caesar cipher principle.

    :param message: The string to be decoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Decoded string.
    """
    return encode(message, -shift, alphabet)


if __name__ == "__main__":
    # simple tests
    print(encode("hello", 1))  # ifmmp
    print(decode("ifmmp", 1))  # hello

    # WRITE THE REMAINING EXAMPLES YOURSELF!

    # larger shift
    print(encode("SomeThing1", 1))

    # negative shift
    print(decode("Sbju1", 1))

    # shift > alphabet.length
    print(decode("Asdf1☻", 1))

    # case sensitivity
    print(encode("AaBbCcDdEeFfGg1", 1))
    print(decode("BbCcDdEeFfGg1", 1))

    # misc symbols (.,:; etc.)
    print(encode("asdfmovieftw1...", 1))
    # ...
    print(encode("Öö", 1))
    print(decode("♥♥♥♦♦♦♣♣♣♠♠♠", 1))
