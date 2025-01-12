class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniques = {}
        repeats = []
        for idx, c in enumerate(s):
            if c in repeats:
                continue

            if c in uniques:
                uniques.pop(c)
                repeats.append(c)
            else:
                uniques[c] = idx

        if not uniques:
            return -1
        
        return min(uniques.values())