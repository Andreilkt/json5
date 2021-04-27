a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
'pet' in a_dict.keys()

b_dict = {'color': 'blue1', 'fruit1': 'apple1', 'pet1': 'dog1'}

for item in a_dict.items():
    print(item)
    print(type(item))



for key, value in a_dict.items():
    print (key, '->', value)

