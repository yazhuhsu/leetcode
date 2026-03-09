class Solution:
    def findJudge(self, n: int, trust: list) -> int:
        if len(trust) == n:
            return -1
        if len(trust) == 0 and n == 1:
            return 1

        judgeDict, trustDict = dict(), dict()
        for _, trusts in enumerate(trust):
            if trusts[0] not in trustDict:
                trustDict[trusts[0]] = []
            if trusts[1] not in judgeDict:
                judgeDict[trusts[1]] = []

            trustDict[trusts[0]].append(trusts[1])
            judgeDict[trusts[1]].append(trusts[0])

        for k, v in judgeDict.items():
            if len(v) != n-1:
                continue
            
            if k not in trustDict:
                return k

        return -1

solution = Solution()
print(solution.findJudge(2, [[1, 2]]) == 2)
print(solution.findJudge(3, [[1, 3], [2, 3]]) == 3)
print(solution.findJudge(3, [[1, 3], [2, 3], [3, 1]]) == -1)