text = "Le fichier se trouve dans le package com.wazaastudio.trainme.ui.trainings." \
       "On peut accéder à cette interface en créant un entrainement (préalablement, " \
       "il doit y avoir des exercices de créer) et en appuyant par la suite sur " \
       "le bouton « Play » de l’entrainement."

new_text = f"Le fichier se trouve dans le package com.wazaastudio.trainme.ui.trainings." \
           f"On peut accéder à cette interface en créant un entrainement (préalablement, " \
 \
    # we can format string to use triple single quote or triple double single double

third_text = """Le fichier se trouve dans le package com.wazaastudio.trainme.ui.trainings.
    On peut accéder à cette interface en créant un entrainement (préalablement, 
    il doit y avoir des exercices de créer) et en appuyant par la suite sur """

# method with concatenation
name = 'Ouzin ' + 'aly'

# method to concat int
somme = "5" + "4"
# method to multiply character
character = "!*" * 5
# print(character)

# string is not immutable
# name[6] = "p"
# print(name)  # 'str' object does not support item assignment

phrase = "Swim, Eat, Sleep"

swimming = phrase[::-1]
print(swimming)
