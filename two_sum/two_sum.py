from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] == target):
                    result.append(i)
                    result.append(j)
                    break
            
            if(len(result) == 2) :
                break
                
        return result

f = open("two_sum.txt", "r+")
r = f.read().splitlines()
for i in range(0, len(r)-1, 2):
    nums = r[i]
    target = r[i+1]
    solution = Solution()
    result = solution.twoSum(eval(nums), int(target))
    print(result)