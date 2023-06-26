#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    try:
        for i in range(x):
            try:
                assert isinstance(my_list[i], int)
                print("{:d}".format(my_list[i]), end="")
                nb_print += 1
            except AssertionError:
                continue
            except IndexError:
                break
        print()
    except TypeError:
        pass

    return nb_print
