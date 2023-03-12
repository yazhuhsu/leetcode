class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabets = [a for a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        if columnTitle in alphabets:
            return alphabets.index(columnTitle)+1

        mods = alphabets.index(columnTitle[-1])+1
        titles = [s for s in columnTitle[:-1]]
        if len(titles) > 1:
            titles.reverse()
        for idx, column in enumerate(titles, start=1):
            mods += (alphabets.index(column)+1) * (26**(idx))

        return mods