#!/usr/bin/python3
"""text indention module"""


def text_indentation(text):
    """text index"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    newline_flag = True

    for char in text:
        if char in ['.', '?', ':']:
            result += char + "\n\n"
            newline_flag = True
        else:
            if newline_flag:
                if char != ' ':
                    result += char
                newline_flag = False
            else:
                result += char

    print(result)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")