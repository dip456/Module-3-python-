""" Write a Python function to check whether a number is perfect or not. """
def is_perfect(number):
    """
    Check if a number is perfect or not.

    Parameters:
        number (int): The number to check.

    Returns:
        bool: True if the number is perfect, False otherwise.
    """
    if number <= 0:
        return False

    divisor_sum = sum([divisor for divisor in range(1, number) if number % divisor == 0])
    return divisor_sum == number

# Test the function
number = 28
print("Is", number, "a perfect number?", is_perfect(number))
