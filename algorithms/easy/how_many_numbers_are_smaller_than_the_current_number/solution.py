class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numMap = dict()
        for idx, num in enumerate(nums):
            if num not in numMap:
                numMap[num] = 0
            numMap[num] += 1

        counts = []
        for idx, num in enumerate(nums):
            counts.append(0)
            for k, v in numMap.items():
                if k < num:
                    counts[idx] += v
        
        return counts

solution = Solution()
print(solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3])
print(solution.smallerNumbersThanCurrent([6, 5, 4, 8]) == [2, 1, 0, 3])
print(solution.smallerNumbersThanCurrent([7, 7, 7, 7]) == [0, 0, 0, 0])