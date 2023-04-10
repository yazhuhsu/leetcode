class Solution:
    def mySqrt(self, x: int) -> int:

        if x in [0, 1]:
            return x

        xs = []
        for n in range(1, x):
            if n*n <= x:
                xs.append(n)
            else:
                break

        return xs[-1]