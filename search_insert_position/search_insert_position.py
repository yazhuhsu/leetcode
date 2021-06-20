class Solution:
    """
    searchInsert

    given a sorted list of distinct integers and a target value
    1. if target found in list: return index
    2. if target not found: return index where it would be
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        # if target larger than largest one: return index+1
        if target > nums[length-1]:
            return length
        # if target smaller than smallest one: return 0
        elif target < nums[0]:
            return 0
        
        # if target equal value in list: return index
        # else: return the index of target should be inserted to
        for index, value in enumerate(nums):
            if value == target:
                return index
            elif index > 0 and value > target:
                if target > nums[index-1]:
                    return index