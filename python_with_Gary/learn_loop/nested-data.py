user_groups = [
    [
        {'name': 'Person A', 'isStudent': True},
        {'name': 'Person B', 'isStudent': True}
    ],
    [
        {'name': 'Person C', 'isStudent': False},
        {'name': 'Person D', 'isStudent': False}
    ]
]

for user_group in user_groups:
    for user in user_group:
        if user["isStudent"]:
            print(f'{user["name"]} is student')
        else:
            print(f'{user["name"]} is not student')
