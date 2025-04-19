HEX_DIGITS = tuple('0123456789ABCDEF')


def is_decimal(x: str): return x.isdecimal()


def is_binary(x: str):
    is_valid = False

    if x.startswith('0b'):
        for n in x[2:]:
            if n in '01':
                is_valid = True
            is_valid = False

    return is_valid


def is_hex(x: str):
    return x.startswith('0x') and all(c in HEX_DIGITS for c in x[2:])


def from_decimal_to_binary(num):
    if not is_decimal(num):
        print('Wrong format!')
        return 0

    num = int(num)

    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    return int(binary)


def from_binary_to_decimal(num: str):
    num = num[2:]

    result = 0

    for i in num:
        result *= 2
        result += int(i)

    return result


def to_decimal(num: str):
    if is_decimal(num):
        return int(num)
    elif is_binary(num):
        return from_binary_to_decimal(num)
    elif is_hex(num):
        result = 0
        power = 0

        for digit in reversed(num[2:].upper()):
            result += HEX_DIGITS.index(digit) * (16 ** power)
            power += 1

        return result
    elif 'x' in num:
        number, base = num.split('x')
        result = 0

        for i in number:
            result *= int(base)
            result += int(i)
        return result

    return 0


def to_hex(num):
    num = to_decimal(num)

    hex_num = ''
    while num > 0:
        remainder = num % 16
        hex_num = HEX_DIGITS[remainder] + hex_num
        num //= 16

    return hex_num


def to_binary(num):
    num = str(to_decimal(num))

    return from_decimal_to_binary(num)


def to_any_base(num: int, base: int):
    result = ''

    while num > 0:
        remainder = num % base
        result = HEX_DIGITS[remainder] + result
        num //= base

    return result


while True:
    user_input = input('Enter a number: ')
    base = int(
        input('What base would you like to convert it to?: '))
    print('\n')

    decimal_number = to_decimal(user_input)

    if decimal_number == 0:
        print('Incorrect format!')
        quit()

    number_in_base = to_any_base(decimal_number, base)

    print(f'Your number in decimal: {decimal_number}')
    print(f'Your number in the specified format: {number_in_base}x{base}')

    user_choice = input('Would you like to start again?: ').lower()
    if user_choice != 'yes' and user_choice != 'y':
        break
