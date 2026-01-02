class Solution:
    def repeatedNTimes(self, nums: list) -> int:
        num_dict = dict()
        for idx, num in enumerate(nums):
            if num in num_dict:
                return num
            
            if num not in num_dict:
                num_dict[num] = True

solution = Solution()
print(solution.repeatedNTimes([1, 2, 3, 3]) == 3)
print(solution.repeatedNTimes([2, 1, 2, 5, 3, 2]) == 2)
print(solution.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]) == 5)