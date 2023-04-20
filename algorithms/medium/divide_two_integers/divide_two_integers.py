class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend > 2**31-1 or dividend < -(2**31) or \
            divisor > 2**31-1 or divisor < -(2**31):
            return 0

        negative = False
        if dividend < 0:
            negative = not negative
            dividend = -(dividend)
        if divisor < 0:
            negative = not negative
            divisor = -(divisor)

        count = 0
        bin_dividend = len(bin(dividend)) - 2
        bin_divisor = len(bin(divisor)) - 2

        while bin_dividend > bin_divisor:
            count += 1 << (bin_dividend - bin_divisor - 1)
            dividend -= divisor << (bin_dividend - bin_divisor - 1)
            bin_dividend = len(bin(dividend)) - 2

        if dividend >= divisor:
            count += 1

        if negative:
            count = -(count)

        if count > 2**31-1:
            count = 2**31-1
        if count < -(2**31):
            count = -(2**31)

        return count