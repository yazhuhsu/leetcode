class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t * 2

solution = Solution()
print(solution.theMaximumAchievableX(4, 1) == 6)
print(solution.theMaximumAchievableX(3, 2) == 7)