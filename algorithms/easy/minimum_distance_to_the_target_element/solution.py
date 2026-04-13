class Solution:
    def getMinDistance(self, nums: list, target: int, start: int) -> int:
        minimized = 1000+start
        for idx, num in enumerate(nums):
            if num != target:
                continue
            
            if minimized > abs(idx-start):
                minimized = abs(idx-start)
            
        return minimized

solution = Solution()
# Target appears on both sides of start, closer one wins
print(solution.getMinDistance([1, 2, 3, 4, 5], 5, 3) == 1)
# Target only appears before start
print(solution.getMinDistance([1, 2, 3, 4, 5], 1, 4) == 4)
# Target is at start index
print(solution.getMinDistance([1, 2, 3, 4, 5], 3, 2) == 0)
# Multiple occurrences of target, pick closest
print(solution.getMinDistance([1, 1, 1, 1, 1], 1, 2) == 0)
# Target at both ends, start in middle
print(solution.getMinDistance([5, 3, 6, 5], 5, 2) == 1)