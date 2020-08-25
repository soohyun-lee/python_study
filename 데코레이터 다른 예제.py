
def bread(func):
    def wrapper():
        print("</'''''\>")
        func()
        print("<\_____/>")
    return wrapper
def ingredients(func):
    def wrapper():
        print("tomato")
        func()
        print("salad~")
    return wrapper
def sandwich (food="--ham--"):
    print(food)

# sandwich()
# sandwich = bread(ingredients(sandwich))
# sandwich()

@bread
@ingredients
def sandwich(food="--ham--"):
    print(food)
sandwich()

def makebold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"
    return wrapper

def makeitalic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"
    return wrapper

@makebold
@makeitalic
def say():
    return "hello"

print(say())


def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1,arg2):
        print(f"i got args! look: {arg1}, {arg2}")
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

@a_decorator_passing_arguments
def print_full_name(firstname, last_name):
    print(f"my name is {firstname},{last_name}")

print_full_name('이','수현')
# i got args! look: 이, 수현
# my name is 이,수현

def my_decorator(func):
    # print("i am on ordinary function")
    def wrapper():
        print('i am function returned by the decorator')
        func()
    return wrapper

# def lazy_function():
#     print('zzzzzz')
# decorated_function = my_decorator(lazy_function)

@my_decorator
def lazy_function():
    print('zzzzz')
