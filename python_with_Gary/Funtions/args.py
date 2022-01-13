def calculate_average(*args):
    return sum(args) / len(args)


node10 = 10
node20 = 20
node30 = 30
node40 = 40

average = calculate_average(node10, node20)


# print(average)


def filter_number(*args):
    return [item for item in args if item > 10]


print(filter_number(1, 5, 10, 8, 15, 7, 12))
