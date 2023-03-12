class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            counts.setdefault(num, 0)
            counts[num] += 1

        for num, count in counts.items():
            if count >= 2:
                return True

        return False