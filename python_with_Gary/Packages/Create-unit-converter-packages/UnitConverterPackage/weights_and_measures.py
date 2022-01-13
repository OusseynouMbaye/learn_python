# - PART III
# -  convert lbs to kg
def lbs_to_kg(unit_amount, inverse=False):
    lbs_per_kg = 2.2046
    if inverse:
        return unit_amount * lbs_per_kg

    return unit_amount / lbs_per_kg


# -  convert cm to inches
def cm_to_inches(unit_amount, inverse=False):
    cm_per_inches = 2.54
    if inverse:
        return unit_amount * cm_per_inches

    return unit_amount / cm_per_inches


def celcius_to_fahrenheit(unit_amount, inverse=False):
    if inverse:
        return (unit_amount - 32) * 5 / 9

    return (unit_amount * 9 / 5) + 32


conversions = {
    '1': {'name': 'lbs to kgs', 'function': lbs_to_kg, 'inverse': False},
    '2': {'name': 'kgs to lbs', 'function': lbs_to_kg, 'inverse': True},
    '3': {'name': 'cm to inches', 'function': cm_to_inches, 'inverse': False},
    '4': {'name': 'inches to cm', 'function': cm_to_inches, 'inverse': True},
    '5': {'name': 'celcius to fahrenheit', 'function': celcius_to_fahrenheit, 'inverse': False},
    '6': {'name': 'fahrenheit to celcius', 'function': celcius_to_fahrenheit, 'inverse': True},
}
