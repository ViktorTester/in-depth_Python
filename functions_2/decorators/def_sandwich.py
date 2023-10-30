"""The sandwich decorator displays the texts:

---- Top slice of bread ----
---- Bottom slice of bread ----

before and after calling the function being decorated, respectively."""


def sandwich(func):
    def wrapper(*args, **kwargs):
        print("---- Top slice of bread ----")
        result = func(*args, **kwargs)
        print("---- Bottom slice of bread ----")
        return result

    return wrapper


@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))


add_ingredients(['tomato', 'salad', 'cheese', 'bacon'])


@sandwich
def sample():
    return 'sample'


print(sample())
