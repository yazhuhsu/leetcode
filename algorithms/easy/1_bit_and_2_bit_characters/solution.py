class Solution:
    def isOneBitCharacter(self, bits: list) -> bool:
        skip = False
        for i in range(0, len(bits)-1):
            if skip:
                skip = False
                continue

            if bits[i] == 1:
                skip = True
                continue

        if skip:
            return False

        return True

solution = Solution()
print(solution.isOneBitCharacter([1,0,0])==True)
print(solution.isOneBitCharacter([1,1,1,0])==False)