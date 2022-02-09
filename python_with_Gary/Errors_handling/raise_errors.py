dividend = 100
divisor = 11  # or 0

try:
    if divisor > 10:
        raise ValueError

    quotient = dividend / divisor
    print(quotient)

except ValueError:
    print("divisor must not be greather")
except Exception as e:
    print(e)
finally:
    print('Process done')
