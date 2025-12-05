class Solution:
    def countPartitions(self, nums: list) -> int:
        even, sum_num = 0, self.sumUp(nums)
        for i in range(0, len(nums)-1):
            left = self.sumUp(nums[0:i])
            right = sum_num - left
            if (left-right) % 2 == 0:
                even += 1

        return even
        
    def sumUp(self, nums: list) -> int:
        count = 0
        for _, num in enumerate(nums):
            count += num

        return count

solution = Solution()
print(solution.countPartitions([10,10,3,7,6])==4)
print(solution.countPartitions([1,2,2])==0)
print(solution.countPartitions([2,4,6,8])==3)