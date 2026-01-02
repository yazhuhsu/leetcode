class Solution:
    def findErrorNums(self, nums: list) -> list:
        num_dict = dict()
        for _, num in enumerate(nums):
            if num not in num_dict:
                num_dict[num] = 0
            
            num_dict[num] += 1
        
        dup, mis = 0, 0
        for i in range(1, len(nums)+1):
            if i not in num_dict:
                mis = i
            if i in num_dict and num_dict[i] > 1:
                dup = i

        return [dup, mis]

solution = Solution()
print(solution.findErrorNums([1, 2, 2, 4]) == [2, 3])
print(solution.findErrorNums([1, 1]) == [1, 2])