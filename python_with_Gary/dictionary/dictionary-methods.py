# dictionary methods
my_dict = {'a': 100, 'b': 200, 'c': 300}

# methods to access keys
# print('a' in my_dict)

# print with in , list
# for _ in my_dict:
#     print(_) # print(list(my_dict))

# 3 methods to access keys in, for and list
# print(200 in my_dict.values())
# print(list(my_dict.values()))
# for _ in my_dict.values():
#     print(_)

# print(my_dict.keys())
# list_dict = list(my_dict.items())[0]
# print(type(list_dict))

# remove item with del or pop
# method with del
# del my_dict['b']
# print(my_dict)

# method with pop
popped_dict = my_dict.pop('b')
print(popped_dict, my_dict)
