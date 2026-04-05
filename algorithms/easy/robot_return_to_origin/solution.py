class Solution:
    def judgeCircle(self, moves: str) -> bool:
        movements = {
            'R': [1, 0],
            'L': [-1, 0],
            'U': [0, 1],
            'D': [0, -1]
        }

        origin = [0, 0]
        for idx in range(len(moves)):
            origin[0] += movements[moves[idx]][0]
            origin[1] += movements[moves[idx]][1]

        if origin[0] == 0 and origin[1] == 0:
            return True

        return False

solution = Solution()
print(solution.judgeCircle("UD") == True)
print(solution.judgeCircle("LL") == False)
print(solution.judgeCircle("UDLR") == True)
print(solution.judgeCircle("") == True)