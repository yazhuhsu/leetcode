class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for idx, n in enumerate(nums):
            if nums[idx] != 0:
                continue

            for i in range(idx, len(nums)):
                if nums[i] == 0:
                    continue

                nums[idx] = nums[i]
                nums[i] = 0
                break
        