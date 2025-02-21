def my_max(digits):
    if digits is None or len(digits) == 0:
        return None

    current_max = digits[0]
    for digit in digits:
        if digit > current_max:
            current_max = digit
    return current_max

def my_is_perfect(digit):
    if digit is None or type(digit) is not int or digit <= 0:
        return False

    return digit == sum([i for i in range(1, digit) if digit % i == 0])

def my_is_prime(digit):
    if digit is None or type(digit) is not int or digit <= 1:
        return False

    for i in range(2, digit):
        if digit % i == 0:
            return False
    return True

def luhn_checksum(number):
    if number is None or type(number) is not int or number <= 0:
        return False

    digits = [int(digit) for digit in str(number)]
    check_digit = digits.pop()

    digits.reverse()

    for i in range(len(digits)):
        if i % 2 == 0:
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9

    total = sum(digits)

    calculated_check_digit = (10 - (total % 10)) % 10

    return calculated_check_digit == check_digit
