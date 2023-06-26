#!/usr/bin/python3
def safe_print_integer(value):
    try:
        assert isinstance(value, int)
        print("{:d}".format(value))
        return True
    except AssertionError:
        return False
