def add_many(*args):
    # print(args)
    return sum(args)


result = add_many(1, 5, 6, )


def system_info(**kwargs):
    print(kwargs)
    if "os" in kwargs:
        print(kwargs['os'])


# system_info(lang='Python', os='windows', memory='1GB')

def combine(*args, **kwargs):
    print(args)
    print(kwargs)


combine(1, 2, 5, lang='Python', os='windows')
