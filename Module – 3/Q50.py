""" Write a Python function to check whether a number is perfect or not. """
def perfect_n(number):
    if number <= 0:
        return False

    div_sum = 0
    
    for divisor in range(1, number):
        if number % divisor == 0:
            divsum += divisor
    
    return div_sum == number

number = 50
print(perfect_n(number))
