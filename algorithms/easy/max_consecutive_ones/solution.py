class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        count, max_count = 0, 0
        for idx, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                if max_count < count:
                    max_count = count
                count = 0

            if idx == len(nums)-1:
                if max_count < count:
                    max_count = count

        return max_count

solution = Solution()
print(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3)
print(solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2)