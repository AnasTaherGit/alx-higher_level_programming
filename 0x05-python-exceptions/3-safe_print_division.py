#!/usr/bin/python3
def safe_print_division(a, b):
    div_num = None
    try:
        div_num = a / b
    except ZeroDivisionError:
        div_num = None
    finally:
        print("Inside result: {}".format(div_num))

    return div_num
