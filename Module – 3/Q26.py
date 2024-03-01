""" Write a Python program to replace last value of tuples in a list. """
def change_last(tuple_list, new_value):
    new_list = []
    for i in tuple_list:
        new_tuple = i[:-1] + (new_value,)
        new_list.append(new_tuple)
    return new_list

list_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
my_value = 100
modifie_list = change_last(list_tuples, my_value)
print("modifie list:", modifie_list)
