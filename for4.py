a_dict = {'one': 'test', 'two': 2, 'thee': 3, 'four': 4}
b_dict = {'one': 'test1', 'two': 'test', 'thee': 8, 'four': 9}
new_dict = {}  # Create a new empty dictionary
for key, value in a_dict.items():
    if value == 'test':
        new_dict[key] = value
for key, value in b_dict.items():
    if value == 'test':
        new_dict[key] = value
print(new_dict)