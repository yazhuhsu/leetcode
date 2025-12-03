class Solution:
    def checkRecord(self, s: str) -> bool:
        absent, late = 0, 0
        is_cons, cons = False, []

        for i in range(0, len(s)):
            if s[i] == 'A':
                absent += 1
            if s[i] == 'L':
                if not is_cons:
                    is_cons = True
                    cons.append(i)
            elif is_cons:
                is_cons = False
                cons.append(i-1)

        if is_cons:
            cons.append(len(s)-1)

        for i in range(0, len(cons), 2):
            if late < cons[i+1]-cons[i]+1:
                late = cons[i+1]-cons[i]+1

        if absent >= 2 or late >= 3:
            return False

        return True

solution = Solution()
print(solution.checkRecord("PPALLP") == True)
print(solution.checkRecord("PPALLL") == False)