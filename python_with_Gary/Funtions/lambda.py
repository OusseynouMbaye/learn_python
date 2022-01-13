urls = ['youtube.com', 'google.com', 'amazon.com']

map_test = list(filter(lambda url: url[:-4], urls))
filter_test = list(map(lambda url: url[:-4], urls))

# print(map_test)
# for url in urls:
#     print(url[:-4])

card_numbers = [
    3456789012476345,
    5452789078476311,
    164587985452633
]

challenge = list(filter(lambda card: len(str(card)) == 16, card_numbers))
print(challenge)
