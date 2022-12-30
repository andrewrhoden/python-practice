###Using a closure, create a function, multiples_of(n) which we can use tocreate generators that
 ##generate multiples of n less than a givennumber.'''
def multiples_of(n):
    def end_zone(p):
        for x in range(1,p):
            if x*n <p:
                yield x*n

    return end_zone





m3 = multiples_of(3)
m3_under30 = m3(30)
m7_under30 = multiples_of(7)(30)

print(type(m3_under30))
# output: <class 'generator'>

print(*m3_under30)
# output: 3 6 9 12 15 18 21 24 27

print(*m7_under30)
# output: 7 14 21 28
###########################################################################################

#1. make_upper – make every letter of a string returned from the decorated
#function uppercase.

#2. print_func_name – print the name of the decorated function before
#executing the function.

def make_upper(fun):
    def innerfunc():
        return fun().upper()
        
    return innerfunc


@make_upper
def hello_world():
    return 'hello young, good day!!'

print(hello_world())


#print_func_name – print the name of the decorated function before executing the function.

def print_func_name(function):
    def func_name():
        print (f"{function.__name__} is running... ")
        return function()
    return func_name

@print_func_name
def my_func():
    print('Python is fun!!')

my_func() # output: my_func is running...
                    #Python is fun


#give_name(name) – concatenate the given name at the end of a string
#returned from the decorated function.

def give_name(name):
    def innerjoin(func):
        def clos():
            return (f"{func() } {name}")
        return clos
    return innerjoin



@give_name('Theresa')
def greeting():
    return 'Hello'

print(greeting()) # output: Hello Theresa


#print_input_type – print a data type of the input argument before executing the decorated function.

def print_input_type(fun):
    def wrapper(n):
        print (f"The input data type is {type(fun(n))}")
        return fun(n)
    return wrapper

@print_input_type
def square(n):
    return n ** 2

print(square(3.5)) # output: The input data type is <class 'float'>

12.25