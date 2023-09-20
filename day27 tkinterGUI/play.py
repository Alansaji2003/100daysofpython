#unlimited positional arguments
def add(*args):
    s = 0
    for n in args: #since args is a tuple we can also use indexing eg: args[0]
        s = s + n ;
    print(s)


add(4,5,6,7,8,9,0,354,543,453,435,324,234,234)

#kwargs
def calc(n, **kwargs):   #key word arguments are dictioary
    # for key, value in kwargs:
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calc(4, add = 2, multiply = 3)