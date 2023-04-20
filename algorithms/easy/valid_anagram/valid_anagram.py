class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        used_s = {}
        for c in s:
            used_s.setdefault(c, 0)
            used_s[c] += 1

        for c in t:
            if c not in used_s:
                break

            used_s[c] -= 1
            if used_s[c] == 0:
                used_s.pop(c)

        if not used_s:
            return True

        return False
