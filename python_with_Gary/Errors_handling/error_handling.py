dividend = 10
divisor = '5'

try:
    quotient = dividend / divisor
    print(quotient)
except ZeroDivisionError as division_by_zero:
    print(division_by_zero)
except TypeError:
    print('division by str')
except Exception as e:
    print(e)
else:
    print('Everything worked')
finally:
    print('Process done')
