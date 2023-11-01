#!/usr/bin/python3
"""text indention module"""


def text_indentation(text):
    """ prints a text with 2 new lines after: . , ? and : """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    newline_flag = True

    for char in text:
        if char in ['.', '?', ':']:
            result += char + "\n\n"
            newline_flag = True
        elif char == ' ' and newline_flag:
                continue
        else:
            result += char
            newline_flag = False

    result = result.replace("\n ", "\n")
    print(result)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
