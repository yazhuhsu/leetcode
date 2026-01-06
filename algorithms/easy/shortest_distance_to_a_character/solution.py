class Solution:
    def shortestToChar(self, s: str, c: str) -> list:
        indices = []
        for idx, r in enumerate(s):
            if r == c:
                indices.append(idx)

        distances = []
        for idx in range(len(s)):
            distance = len(s)
            for _, ind in enumerate(indices):
                if abs(idx-ind) < distance:
                    distance = abs(idx-ind)
            distances.append(distance)

        return distances

solution = Solution()
print(solution.shortestToChar("loveleetcode", "e") == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])
print(solution.shortestToChar("aaab", "b") == [3, 2, 1, 0])