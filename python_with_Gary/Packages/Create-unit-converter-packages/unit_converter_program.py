from UnitConverterPackage import weights_and_measures

# - PART II
# - Add functionality for selecting module category
#      - create a module_options dictionary
#      - build up the input message dynamically using values from module_options
#      - get the user input
#      - if the selected option is invalid, ask again

module_options = {
    '1': {'name': 'Weights and Measures', 'module': weights_and_measures}
}
category_choice_string = 'Please select a number from following categories : '

for key, module_dict in module_options.items():
    category_choice_string += f"\n[{key}] {module_dict['name']}"

category_choice_string += '\n> '

chosen_category = ''

while chosen_category not in module_options.keys():
    chosen_category = input(category_choice_string)

conversions = module_options[chosen_category]['module'].conversions

conversions_choice_string = 'Please select a number from following options: '

for key, conversion in conversions.items():
    conversions_choice_string += f'\n[{key}] {conversion["name"]}'

conversions_choice_string += '\n> '

chosen_conversion = ''

while chosen_conversion not in conversions.keys():
    chosen_conversion = input(conversions_choice_string)
