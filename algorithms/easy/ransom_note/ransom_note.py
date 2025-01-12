class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazines = [m for m in magazine]

        for r in ransomNote:
            if r in magazines:
                magazines.remove(r)
            else:
                return False

        return True