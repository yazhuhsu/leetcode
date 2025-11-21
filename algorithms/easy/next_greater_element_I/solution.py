class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        find, ans = False, []
        for idx, num1 in enumerate(nums1):
            find = False
            for num2 in nums2:
                if num2 == num1:
                    find = True
                    continue

                if find and num2 > num1:
                    ans.append(num2)
                    break
            
            if len(ans) != idx + 1:
                ans.append(-1)

        return ans

solution = Solution()
print(solution.nextGreaterElement([4,1,2], [1,3,4,2]) == [-1,3,-1])
print(solution.nextGreaterElement([2,4], [1,2,3,4]) == [3,-1])