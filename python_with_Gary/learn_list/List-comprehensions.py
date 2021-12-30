# my_list = []
# for letter in 'word':
#     my_list.append(letter)

# another method to append in list
# my_list = [letter for letter in 'word']
# print(my_list)

# my_list = []
# for number in range(1, 11):
#     print(my_list.append(number * 2))


my_list = [number * 2 for number in range(1, 11)]
# print(my_list)

high_numbers = [number for number in range(1, 10) if number > 5]
# print(high_numbers)

even_list = [number for number in range(1, 101) if number % 2 == 0]
print(even_list)
