#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        if result is None:
            raise TypeError
    except TypeError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return (result)
