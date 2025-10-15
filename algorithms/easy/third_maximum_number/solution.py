class Solution:
    def thirdMax(self, nums: list) -> int:
        num_dict = dict()
        for idx, num in enumerate(nums):
            if num not in num_dict:
                num_dict[num] = True

        first, second, third = -2**31-1, -2**31-1, -2**31-1
        for num, _ in num_dict.items():
            if num > first:
                if second != -2**31-1:
                    third = second
                if first != -2**31-1:
                    second = first
                first = num
            elif num > second:
                if second != -2**31-1:
                    third = second
                second = num
            elif num > third:
                third = num

        if third == -2**31-1:
            return first
        
        return third

print(Solution().thirdMax([3, 2, 1]) == 1)
print(Solution().thirdMax([1, 2]) == 2)
print(Solution().thirdMax([2, 2, 3, 1]) == 1)