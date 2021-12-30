def divisble_number(lowest_number: int, higher_number: int, divisor: int):
    my_list = [item for item in range(lowest_number, higher_number)
               if item % divisor == 0]
    # for item in range(lowest_number, higher_number):
    #     if item % divisor == 0:
    #         my_list.append(item)
    return my_list


print(divisble_number(5, 50, 8))
