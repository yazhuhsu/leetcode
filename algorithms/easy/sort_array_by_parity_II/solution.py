class Solution:
    def sortArrayByParityII(self, nums: []) -> []:
        odds, evens = [], []
        for idx, num in enumerate(nums):
            if idx % 2 == 0 and num % 2 != 0:
                odds.append(idx)
                continue
            if idx % 2 != 0 and num % 2 == 0:
                evens.append(idx)

        for idx in range(len(odds)):
            odd, even = nums[odds[idx]], nums[evens[idx]]
            nums[odds[idx]] = even
            nums[evens[idx]] = odd

        return nums

solution = Solution()
print(solution.sortArrayByParityII([4, 2, 5, 7]) == [4, 5, 2, 7])
print(solution.sortArrayByParityII([2, 3]) == [2, 3])