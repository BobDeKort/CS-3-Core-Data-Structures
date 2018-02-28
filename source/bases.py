#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    # inital thoughts
    # result = 0
    # lenght = len(digits)
    # for idx, d in range(lenght, 0, -1):
    #     result += d * base**idx
    #
    # return result
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    letters_dict = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14,
                    'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21}

    number_array = []
    result = 0

    # reversing our string, because computers read from left to right
    digits = ''.join(reversed(digits))
    for index, value in enumerate(digits):
        letter_value = 0
        # looping through our string
        # check if the value is a letter, if it matches anything in our
        # letters_dict, pull that value
        if digits[index].isalpha():
            letter_value = ord(digits[index]) - 87

        # if it's not a letter, just pull the value and make it an int
        else:
            letter_value = int(value)
        # now at the end of each loop, multiply our value by what the base is
        # to the index power
        base_index = pow(base, index)
        num = letter_value * base_index
        number_array.append(num)

    # after getting our number array, loop through the array in add up
    # everything
    for num in number_array:
        result += num
    return int(result)

    return number_array


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    power = 0
    digit = 0
    result = ""
    # First we have to see which base power to start with

    while pow(base, power) < number:
        power += 1
    # At this point we know where to start from, now we see how many times that base_power goes into our number
    # We want to loop backwards from our current power to 0

    while power >= 0:
        # If Else logic: We are incrementing our digit until we the value is greater than our current number
        # This will make the current digit the largest possible digit for that base_power
        # And after we get the largest possible digit, we check if that digit is bigger than 10 for the letter and
        # Add it to our string

        # if the base_power is less than or equal to the current number
        if pow(base, power) <= number:
            digit += 1
            number -= pow(base, power)
        # When our base_power is greater than the current number
        else:
            # Here we will add the current digit to our result
            # we may have to check if it will become a letter
            if digit >= 10:
                digit = chr(digit + 87)
            print(digit)
            result += str(digit)
            if result == "0":
                result = ""

            digit = 0
            power -= 1
    if result == '':
        result = '0'

    return result


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    base_ten = decode(digits, base1)
    result = encode(base_ten, base2)
    return result


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(
            digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
