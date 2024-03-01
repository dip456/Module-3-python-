""" Write a Python program to remove an empty tuple(s) from a list of tuples. """
def remove_empty(tuples_list):
    res = []
    for i in tuples_list:
        if i:
            res.append(i)
    return res
list = [(1, 2, 3), (), (4, 5), (), (6), ()]
new_list = remove_empty(list)
print("original list:",list)
print("modified list:",new_list)
