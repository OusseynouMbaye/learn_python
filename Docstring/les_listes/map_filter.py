my_list = [1, 2, 3, 4, 5]

# r = map(lambda x: x * x, my_list)  # on multiplie chaque valeur par lui meme
# print(list(r))
#
# r = [i * i for i in my_list]
# print(r)

f = filter(lambda x: x % 2 == 0, my_list)
print(list(f))

f = [i for i in my_list if i % 2 == 0]
print(f)
