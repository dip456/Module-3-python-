""" Write a Python function to check whether a number is perfect or not. """
def perfect_n(number):
   
    if number <= 0:
        return False

    divisor_sum = sum([divisor for divisor in range(1, number) if number % divisor == 0])
    return divisor_sum == number

number = 28
print(perfect_n(number))
