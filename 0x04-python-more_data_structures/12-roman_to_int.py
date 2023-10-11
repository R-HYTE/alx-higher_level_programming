#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check if the input is a non-empty string; if not, return 0
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    # Dictionary mapping Roman numerals to their respective values
    roman_to_int = {'I': 1, 'V': 5, 'X': 10,
                    'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Initialize total sum and previous value
    total = 0
    prev = 0
    # Iterate through the reversed Roman numeral string
    for rep in reversed(roman_string):
        current = roman_to_int[rep]  # Get value of the current Roman numeral

        # If the current value is >= to the previous value, add to the total
        if current >= prev:
            total += current
        else:
            # If the current value is < the previous value, subtract from total
            total -= current
        # Update the previous value for the next iteration
        prev = current

    return total
