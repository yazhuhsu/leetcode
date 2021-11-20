class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        j = nums[0]
        i = 1
        while(i < len(nums)):
            if nums[i] == j:
                del nums[i]
            elif j < nums[i]:
                j = nums[i]
                i += 1
            
            if i == len(nums):
                break
        return len(nums)
        