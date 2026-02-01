class Solution:
    def minimumCost(self, nums: list) -> int:
        nums[1:] = sorted(nums[1:])

        return nums[0]+nums[1]+nums[2]

solution = Solution()
print(solution.minimumCost([1, 2, 3, 12]) == 6)
print(solution.minimumCost([10, 3, 1, 1]) == 12)
print(solution.minimumCost([5, 4, 3]) == 12)