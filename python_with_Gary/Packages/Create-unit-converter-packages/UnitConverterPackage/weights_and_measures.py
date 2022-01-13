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

    return (unit_amount * 9/5) + 32
