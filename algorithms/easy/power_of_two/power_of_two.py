class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        nx = 0
        for x in range(n):
            if x == 0:
                nx = 1
            else:
                nx *= 2

            if nx == n:
                return True
            if nx > n:
                return False