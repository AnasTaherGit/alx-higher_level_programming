#!/usr/bin/python3
import importlib


def main():
    module = importlib.import_module('hidden_4')
    names = list(filter(lambda name: not name.startswith("__"), dir(module)))
    names.sort()
    for name in names:
        print(name)


if __name__ == "__main__":
    main()
