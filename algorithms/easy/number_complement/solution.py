class Solution:
    def findComplement(self, num: int) -> int:
        num_str = ''
        while num != 0:
            if num % 2 == 1:
                num_str = '0'+num_str
            else:
                num_str = '1'+num_str

            num = int(num/2)

        s, c = 0, 1
        nums = list(num_str)
        for i in range(0, len(num_str)):
            if nums[len(nums)-1-i] == '1':
                s += c
            
            c *= 2

        return s
        
solution = Solution()
print(solution.findComplement(5) == 2)
print(solution.findComplement(1) == 0)