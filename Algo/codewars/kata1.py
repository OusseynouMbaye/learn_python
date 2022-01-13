# Description:
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
#
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
#
# Note: The function accepts an integer and returns an integer

# num = 9119  result 811181
# test 2 cases = [(3212, 9414), (2112, 4114), (0,0)]
def square_digits(num):
    list_num = [int(i) * int(i) for i in str(num)]
    str_list_num = ''.join([str(i) for i in list_num])
    return int(str_list_num)
