class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        t_list = list(t)

        for v in s:
            if v in t_list:
                t_list.remove(v)
            else:
                return v

        return t_list[0]
        