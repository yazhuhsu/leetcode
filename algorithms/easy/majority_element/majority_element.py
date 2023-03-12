class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counts = {}

        for num in nums:
            counts.setdefault(num, 0)
            counts[num] += 1

        for num, count in counts.items():
            if count > n//2:
                return num