class Solution:
    def maximumProduct(self, nums: list) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        nums.sort()

        counts = []
        for _, num in enumerate(nums[:3]):
            if num > 0:
                break
            
            counts.append(num)

        min_product, max_product = 0, nums[-3]*nums[-2]*nums[-1]
        if len(counts) >= 2:
            min_product = counts[0] * counts[1] * nums[-1]

        if min_product > max_product:
            return min_product
        else:
            return max_product

solution = Solution()
print(solution.maximumProduct([1, 2, 3])==6)
print(solution.maximumProduct([1, 2, 3, 4])==24)
print(solution.maximumProduct([-1, -2, -3])==-6)
print(solution.maximumProduct([-34, 1, 2, 3, 4, 5])==60)
print(solution.maximumProduct([-34, -33, 2, 3, 4, 5])==5610)
print(solution.maximumProduct([-100, -98, -1, 2, 3, 4])==39200)
print(solution.maximumProduct([-100, -2, -3, 1])==300)