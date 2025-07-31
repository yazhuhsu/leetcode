class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # count the number of each rune in the string
        runes = dict()
        for rune in s:
            runes[rune] = runes.get(rune, 0) + 1

        # count the number of the rune
        count, mid = 0, False
        for _, v in runes.items():
            # even, add the number of the rune
            if v % 2 == 0:
                count += v
            else:
                # odd, add the number of the rune - 1
                count += v - 1
                # odd, put one rune in the middle
                if not mid:
                    count += 1
                    mid = True

        return count

cases = {
    # 1. runeMap = {a: 1, b: 1, c: 4, d: 2}
    # 2. iterate, a in the middle
    # 3. iterate, b not in palindrome
    # 4. iterate, c, add 4, start = cc, end = cc
    # 5. iterate, d, add 2, start = ccd, end = dcc
    # 6. return 7, ccdadcc/dccaccd
    "abccccdd": 7,
    "a": 1,
    "ccc": 3,
}

for k, v in cases.items():
    solution = Solution()
    print(solution.longestPalindrome(k) == v)