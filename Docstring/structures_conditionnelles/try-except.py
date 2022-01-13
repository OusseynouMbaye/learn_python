a = 10
b = 5
try:
    resultat = a / b
except ZeroDivisionError:
    print("division par zero impossible")
except TypeError as t:
    print("Error: ", t)
except NameError as e:
    print("Error", e)
finally:
    print("fin du bloc")
