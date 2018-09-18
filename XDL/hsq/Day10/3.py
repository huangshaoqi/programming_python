from functools import wraps


def outer(func):
    """
    1.This is outer function doc
    """
    print("1This is outer function\n", outer.__name__, outer.__doc__)

    @wraps(func)
    def inner():
        """
        2.This is inner function doc
        """
        print("2This is inner function\n", inner.__name__, inner.__doc__)
        func()

    return inner


@outer
def custom_func():
    """
    3.This is custom function doc
    """
    print("3This is custom function\n", custom_func.__name__, custom_func.__doc__)


custom_func()
print("#########################")
print(custom_func.__name__, custom_func.__doc__)
