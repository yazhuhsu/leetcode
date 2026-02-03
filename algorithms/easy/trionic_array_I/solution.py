class Solution:
    def isTrionic(self, nums: int) -> bool:
        p, q, n = 0, 0, len(nums) - 1
        for idx, num in enumerate(nums):
            if idx == 0:
                continue
            if num < nums[idx - 1] and p == 0:
                p = idx - 1
            if num > nums[idx - 1] and p != 0 and q == 0:
                q = idx - 1
                break

        if p == 0 or q == 0:
            return False

        for i in range(1, p + 1):
            if nums[i] <= nums[i - 1]:
                return False

        for i in range(p + 1, q + 1):
            if nums[i] >= nums[i - 1]:
                return False

        for i in range(q + 1, n + 1):
            if nums[i] <= nums[i - 1]:
                return False

        return True

solution = Solution()
print(solution.isTrionic([1, 3, 5, 4, 2, 6]) == True)
print(solution.isTrionic([2, 1, 3]) == False)
print(solution.isTrionic([8, 8, 2, 6]) == False)