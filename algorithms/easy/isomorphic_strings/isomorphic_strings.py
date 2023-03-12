class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ss = [sub_s for sub_s in s]
        ts = [sub_t for sub_t in t]

        replacement = {}
        for sub_ss, sub_ts in zip(ss, ts):
            if sub_ss in replacement and replacement[sub_ss] != sub_ts:
                return False

            if sub_ss not in replacement and sub_ts in replacement.values():
                return False
            
            replacement[sub_ss] = sub_ts

        new_t = ""
        for sub_ss in ss:
            if sub_ss not in replacement:
                return False

            new_t += replacement[sub_ss]

        if new_t == t:
            return True

        return False
