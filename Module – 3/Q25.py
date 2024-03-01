"""Write a Python program to reverse a tuple. """
def rev_tuple(my_tuple):
    rev = tuple(reversed(my_tuple))
    return rev
tuple_list = (10,20,30,50)
new_tuple = rev_tuple(tuple_list)
print("reversed : ",new_tuple)
