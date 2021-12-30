user_groups = [
    [
        {'name': 'Person A', 'isStudent': True},
        {'name': 'Person B', 'isStudent': False}
    ],
    [
        {'name': 'Person C', 'isStudent': False},
        {'name': 'Person D', 'isStudent': True}
    ]
]

for user_group in user_groups:
    # print(user_group)
    for user in user_group:
        # print(user)
        if user["isStudent"]:
            continue
        else:
            print(f'{user["name"]} is not student')
