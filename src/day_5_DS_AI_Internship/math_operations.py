def power(base, exp):
    return base ** exp


def average(numbers_list):
    if len(numbers_list) == 0:
        return 0
    return sum(numbers_list) / len(numbers_list)
