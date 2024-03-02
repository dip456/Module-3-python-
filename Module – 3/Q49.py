""" Write a Python function to check whether a number is in a given range """
def in_range(number, lower_b, upper_b):
   
    return lower_b <= number <= upper_b

number = 7
lower_bound = 5
upper_bound = 10
print( in_range(number, lower_bound, upper_bound))
