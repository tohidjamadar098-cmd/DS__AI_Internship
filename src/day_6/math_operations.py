# math_operations.py

def power(base, exp):
    """Returns base raised to the power of exp."""
    return base ** exp


def average(numbers_list):
    """Returns the average of a list of numbers."""
    if len(numbers_list) == 0:
        return 0
    return sum(numbers_list) / len(numbers_list)
