#!/usr/bin/python3

if __name__ == "__main__":
    # Import the add function from add_0.py
    from add_0 import add
    a = 1
    b = 2

    # Call the add function and print the result using the specified format
    print("{} + {} = {}".format(a, b, add(a, b)))
