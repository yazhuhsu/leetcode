class Solution:
    """
    addBinary

    given two binary strings a and b,
    return sum of a and b as a binary string

    Example1:
    Input:  a = '11', b = '1'
    Output: '100'

    Example2:
    Input:  a = '1010', b = '1011'
    Output: '10101'
    """
    def addBinary(self, a: str, b: str) -> str:

        decimal_a = int(a, 2)
        decimal_b = int(b, 2)
        
        decimal_sum = decimal_a + decimal_b
        binary_sum = "{0:b}".format(decimal_sum)

        return binary_sum