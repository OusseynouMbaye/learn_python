from os import readlink


number = [1,2,3,5,6,3,2,1,4,3]
# method insert(index a laquelle on veut inserer,element a inserer)
number.insert(3,4)
# print(number)
#  method remove :efface le premier l'element demande 
# exemple ici il va enlever le premier 2 rencontrer
number.remove(3)
print(number)
# method pop() removes the item at the given index from the list and returns the removed item.
number.pop(0)
print(number)
# method  count() :return the number of times the specified element appearsin the list
count = number.count(3)
print(count)
