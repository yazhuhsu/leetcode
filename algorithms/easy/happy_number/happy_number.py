class Solution:
    def isHappy(self, n: int) -> bool:
        nums = []
        while n != 1:

            n_to_str = str(n)
            n = 0
            for s in n_to_str:
                n += int(s)*int(s)

            if n == 1:
                return True
            if n in nums:
                return False

            nums.append(n)

        return True