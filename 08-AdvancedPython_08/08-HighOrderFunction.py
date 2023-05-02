def deco(x):

    def y(*args, **kwargs):
        print('********')
        x(*args, **kwargs)
        print('********')

    return y


@deco
def hey(sth, emoji='😮'):
    print(sth, emoji)


hey('heyyyea')
