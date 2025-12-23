class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        for i in range(right-left+1):
            if self.isDivided(left+i):
                nums.append(left+i)

        return nums
        
    def isDivided(self, num: int) -> bool:
        num_dict = {}
        strs = list(str(num))
        for i in range(len(strs)):
            num_dict[int(strs[i])] = True

        for n, _ in num_dict.items():
            print(n)
            if n == 0:
                return False
            if num % n != 0:
                return False

        return True

solution = Solution()
print(solution.selfDividingNumbers(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])
print(solution.selfDividingNumbers(47, 85) == [48, 55, 66, 77])