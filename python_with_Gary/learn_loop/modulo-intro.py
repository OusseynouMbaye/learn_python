
# modulo : retu rest of divide
result = 9 % 2
# print(result)
# floor // : return the exactly result
result = 12//4
# print(result)

evens = list()
odd = list()
# print(evens)
for _ in range(1, 101):
    if _ % 2 == 0:
        evens.append(_)
    else:
        odd.append(_)
print("Odd :", odd)
print("Even : ", evens)
