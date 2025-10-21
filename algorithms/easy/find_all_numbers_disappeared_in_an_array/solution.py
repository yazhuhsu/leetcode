class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        numDict = dict()
        for num in nums:
            if not num in numDict:
                numDict[num] = True

        disappeared = []
        for i in range(1, len(nums)+1):
            if not i in  numDict:
                disappeared.append(i)


        return disappeared


print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6])
print(Solution().findDisappearedNumbers([1, 1]) == [2])