import helpers

tld = 'youtube.com'

shortened = helpers.remove_tld(tld)
numbers = 14235

check_number = helpers.check_len(numbers,5)

print(check_number)
