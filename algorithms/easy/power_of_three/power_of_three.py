class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n in [0, -1]:
            return False

        while n >= 3:
            n /= 3

        if n in [1, -1]:
            return True

        return False