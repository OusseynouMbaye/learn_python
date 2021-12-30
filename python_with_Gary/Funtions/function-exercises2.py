def fizzbuzzer(limit, fizz=3, buzz=5):
    for fizzbuzz in range(limit):
        if fizzbuzz % fizz == 0 and fizzbuzz % buzz == 0:
            print("fizzbuzz")
            continue
        elif fizzbuzz % fizz == 0:
            print('fizz')
            continue
        elif fizzbuzz % buzz == 0:
            print('buzz')
            continue
        print(fizzbuzz)


fizzbuzzer(101, 5, 9)
