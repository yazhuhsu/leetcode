class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = -2**31-1
        ranges = []
        for idx, num in enumerate(nums):
            if start == -2**31-1:
                start = num

            if (idx+1 < len(nums) and nums[idx+1] != num+1) or \
                idx+1 == len(nums):
                if start == num:
                    ranges.append(f"{num}")
                else:
                    ranges.append(f"{start}->{num}")

                start = -2**31-1

        return ranges