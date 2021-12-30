
def remove_duplicates_item(items):
    my_set = set(items)
    return list(my_set)                   # list(dict.fromkeys(x))


my_list = ['Gary', 'Clarke', 'Tech', 'Gary', 'Clarke', 'Tech']
# my_set = set(my_list)
# print(list(my_set))
# quit()
list_remove = remove_duplicates_item(my_list)
print(list_remove)
