class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n in [0, -1]:
            return False

        while n >= 4:
            n /= 4

        if n in [1, -1]:
            return True

        return False