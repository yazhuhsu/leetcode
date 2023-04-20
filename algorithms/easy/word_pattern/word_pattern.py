class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(" ")):
            return False

        pattern_to_s = {}
        for p, c in zip(pattern, s.split(" ")):
            if p not in pattern_to_s:
                if c in pattern_to_s.values():
                    return False
                pattern_to_s[p] = c
            else:
                if pattern_to_s[p] != c:
                    return False

        return True