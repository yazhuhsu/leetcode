class Solution:
    def largeGroupPositions(self, s: str) -> []:
        groups = []
        letter, start, end = "", -1, -1
        for idx, l in enumerate(s):
            if l == letter:
                end = idx
            else:
                if end - start + 1 >= 3:
                    groups.append([start, end])
                letter, start, end = l, idx, idx

        if end == len(s) - 1 and end - start + 1 >= 3:
            groups.append([start, end])

        return groups

solution = Solution()
print(solution.largeGroupPositions("abbxxxxzzy") == [[3, 6]])
print(solution.largeGroupPositions("abc") == [])
print(solution.largeGroupPositions("abcdddeeeeaabbbcd") == [[3, 5], [6, 9], [12, 14]])
print(solution.largeGroupPositions("aaa") == [[0, 2]])