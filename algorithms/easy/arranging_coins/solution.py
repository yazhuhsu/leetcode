class Solution:
    def arrangeCoins(self, n: int) -> int:
        s = 0
        for i in range(1, 2**32):
            if n == s + i:
                return i
            elif n > s and n < s+i:
                return i-1

            s += i 

print(Solution().arrangeCoins(5) == 2)
print(Solution().arrangeCoins(8) == 3)