urls = ['youtube.com', 'google.com', 'amazon.com']


def remove_tld(url):
    return url[:-4]


# for url in map(remove_tld, urls):
#     print(url)

shortened = set(map(remove_tld, urls))  # cast to list , tuple and set
# print(shortened)

card_numbers = [
    3456789012476345,
    5452789078476311,
    164587985452633
]

card_number = [i for i in card_numbers if len(str(i)) == 16]
print(card_number)


def check_list(card):
    return len(str(card)) == 16


card_numbs = filter(check_list, card_numbers)
print(list(card_numbs))
