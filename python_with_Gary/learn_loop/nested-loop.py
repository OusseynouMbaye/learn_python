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
    # print(user_group)
    for user in user_group:
        # print(user)
        if user["isStudent"]:
            print(f'{user["name"]} is student')
        else:
            print(f'{user["name"]} is not student')
