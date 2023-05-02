user1 = {'name': 'Sorokin', 'valid': True}


def authenticated(fn):
    def a(*args, **kwargs):
        if (args[0]['valid']):
            return fn(*args, **kwargs)

    return a


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
