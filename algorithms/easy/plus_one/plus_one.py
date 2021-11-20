class Solution:
    """
    plusOne

    given a non-empty array of decimal digits representing a non-negative integer,
    increment one to the integer.

    Example 1.
    Input:  digits = [1,2,3]
    Output: [1,2,4]

    Example 2.
    Input:  digits = [4,3,2,1]
    Output: [4,3,2,2]

    Note that: integer in python3 is unbounded.
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        digit_len = len(digits)
        number = 0
        for index, digit in enumerate(digits,1):
            number += digit * pow(10, digit_len-index)
            
        number += 1

        digit_output = [int(digit) for digit in str(number)]
            
        return digit_output