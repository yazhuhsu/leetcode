class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        while num >= 10:
            output = 0
            for n in str(num):
                output += int(n)

            if output < 10:
                break

            num = output

        return output