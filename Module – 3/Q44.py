"""Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary. 
Sample data: {'1': ['a','b'], '2': ['c','d']} 
Expected Output: 
ac ad bc bd """

def combinations_from_dict(dictionary):
    values = list(dictionary.values())
    
    combinations = []

    for letter1 in values[0]:
        for letter2 in values[1]:
            combinations.append(letter1 + letter2)

    return combinations

sample_data = {'1': ['a', 'b'], '2': ['c', 'd']}

combinations = combinations_from_dict(sample_data)
print("Expected Output:")
print(" ".join(combinations))
