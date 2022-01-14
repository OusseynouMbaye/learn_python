def kilometers_to_miles(unit_amount, inverse=False):
    kilometers_per_miles = 1.60934
    if inverse:
        return unit_amount * kilometers_per_miles

    return unit_amount / kilometers_per_miles


def kph_to_mph(unit_amount, inverse=False):
    return kilometers_to_miles(unit_amount, inverse)


conversions = {
    '1': {'name': 'kilometers to miles', 'function': kilometers_to_miles, 'inverse': False},
    '2': {'name': 'miles to kilometers', 'function': kilometers_to_miles, 'inverse': True},
    '3': {'name': 'kph to mph', 'function': kph_to_mph, 'inverse': True},
    '4': {'name': 'mph to kph', 'function': kph_to_mph, 'inverse': True},
}
