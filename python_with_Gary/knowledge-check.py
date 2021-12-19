# 1. Calculate 10 cubed
# print(10 ** 3)

url = "garyclarke.tech"
# print(url[:-5])

name = 'Ouzinem'
phrase = 'Hello my name is'
# print(f'{phrase} {name}')

my_list = ['Apple', 'Microsoft', 'Amazon', 'Google']
removed_item = my_list.pop(2)
# print(removed_item, my_list)
# for index, val in enumerate(my_list):
#     print(index, val)

# nexted
info = {
    'software': ['VSCode', 'Pycharm'],
    'programming-langage': ['PHP', 'Python', 'JavaScript']
}
# print(info['programming-langage'][1])

# convert tuple to list
my_tuple = ('Sofia', 'Amina', 'Sarah')
my_liste = list(my_tuple)
# print(my_liste)
# unpacking
Sofia, Amina, Sarah = my_liste


# print(Sofia)
def is_divisible(num1, num2):
    return num1 % num2 == 0


# print(is_divisible(10, 5))

bools_one = 9 % 4 > 2 or 100 not in range(1, 100)
# print(bools_one)
bools_two = 1 + 3 ** 4 < 100 \
            and len(info['software']) not in {'a': 1, 'b': 2, 'c': 3}

print(bools_two)