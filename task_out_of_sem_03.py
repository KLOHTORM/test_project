def f(*args):
    return sum(args)


print(f(1, 2, 3, 4, 5))

print((lambda *args: sum(args))(1, 2, 3, 4, 5))

func = lambda *args: sum(args)
print(func(1, 2, 3, 4, 5))


def fun(**kwargs):
    # return kwargs['a'] + kwargs['b'] + kwargs['c'] + kwargs['d'] + kwargs['e']
    return sum(kwargs.values())
print(fun(a=1, b=2, c=3, d=4, e=5))
