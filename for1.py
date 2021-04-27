
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
b_dict = {'color': 'blue1', 'fruit1': 'apple1', 'pet1': 'dog1'}
for key in a_dict:
    print(key)
for key in a_dict:
    print(key, '->', a_dict[key])
for item in a_dict.items():
    print(item)
for item in b_dict.items():
    print(item)
#if(a_dict < b_dict):
    #print('test')
for item in a_dict.items():
    print(item)
    print(type(item))