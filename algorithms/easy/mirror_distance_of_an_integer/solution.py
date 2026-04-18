class Solution:
    def mirrorDistance(self, n: int) -> int:
        copy, mirror = n, 0
        for i in range(1, len(str(n))+1):
            mirror += int(copy % 10) * int(10**(len(str(n))-i))
            copy = int(copy / 10)            

        if mirror > n:
            return mirror - n

        return n - mirror

solution = Solution()
# Walkthrough example
print(solution.mirrorDistance(1234) == 3087)
# Palindrome: mirror equals n
print(solution.mirrorDistance(1221) == 0)
# Leading zeros dropped in mirror: 100 → 001 = 1
print(solution.mirrorDistance(100) == 99)
# Single digit: mirror equals itself
print(solution.mirrorDistance(7) == 0)
# Mirror is larger than n
print(solution.mirrorDistance(123) == 198)