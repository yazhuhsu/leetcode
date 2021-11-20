from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        min_size = 100**100
        min_pos = 0

        for i in range (0, len(strs)):
            if len(strs[i]) < min_size:
                min_size = len(strs[i])
                min_pos = i

        min_strs = list(strs[min_pos])
        
        same = True
        pos = 0
        for j in range(0, min_size):
            for k in range(0, len(strs)):
                m = list(strs[k])
                if m[j] != min_strs[j]:
                    same = False
            if same != True:
                break
            pos+=1
        
        result = ''
        for l in range(0, pos):
            result += min_strs[l]

        return result