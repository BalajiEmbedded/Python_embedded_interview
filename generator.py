def gen():
    yield 1
    yield 2
    yield 3

obj=gen()
print(next(obj))
print(next(obj))

