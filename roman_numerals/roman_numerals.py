"""
Roman numerals are a sequence of characters used for counting, and for recording what number sequel a movie is.
Valid roman numerals are:

| numeral | value |
| ------- | ----- |
| I       | 1     |
| V       | 5     |
| X       | 10    |
| C       | 100   |
| M       | 1000  |

Roman numerals are written by expressing each digit separately starting with the left most digit:

```
X = 10
VI = 5 + 1 = 6
MXVII = 1000 + 10 + 5 + 1 + 1 = 1017
```

There are some other rules around roman numerals which we don't currently care about.

Write a python program which takes a series of roman numerals as input and which outputs their value as a number.
"""

# store as dict so can easily be accessed
roman_numerals_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def get_user_input():
    
    input_roman_numerals = str(input("Please enter roman numerals: "))
    input_roman_numerals = input_roman_numerals.strip().upper()
        
    # check the user provided valid values
    for numeral in list(input_roman_numerals):
        if numeral not in roman_numerals_values:
            raise ValueError(f"You have provided a value of {numeral} which is not a valid roman numeral")
        
    return input_roman_numerals

def translate_roman_numerals_to_value(roman_numerals):
    
    # storage
    total = 0
    
    # loop through each numeral to get its value, append to storage
    for numeral in roman_numerals:
        value = roman_numerals_values[numeral]
        total += value
        
    return total

def main():
    
    try:
        roman_numerals = get_user_input()
        value = translate_roman_numerals_to_value(roman_numerals)
        print(f"The value for roman numeral {roman_numerals} is {value}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()