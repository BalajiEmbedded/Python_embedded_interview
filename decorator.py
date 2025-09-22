def decor(fun):
    def wrapper():
        print('decorating')
        fun()
        print('decorated')
    return wrapper
@decor
def logs():
    print('logs')
logs()