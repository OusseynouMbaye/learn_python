my_set = set()

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
evens = set()
odds = set()

for num in my_list:
    if num % 2 == 0:
        evens.add(num)
        even_sorted = sorted(evens)
    else:
        odds.add(num)


# print("evens number is {e}".format(e=evens))
# print("odds number is {o}".format(o=odds))
print(set(my_list))
