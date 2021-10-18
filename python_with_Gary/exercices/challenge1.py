star_rating = [4,2,3,5,4,1,3,4,5,1]
number_input = int(input("Enter a nombre between 1 to 5 : "))
number = number_input
print("The number you enter is " , number)
star_rating.append(number)
print(star_rating)
number_to_average =  star_rating[-5:]

def average_star(array_number):
   return sum(array_number)/len(array_number)

value_star = average_star(number_to_average)

print("the average of last 5 number is ", value_star)