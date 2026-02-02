class Solution:
    def lemonadeChange(self, bills: list) -> bool:
        changes = dict()
        for _, cost in enumerate(bills):
            change = cost - 5
            while change >= 10:
                if 10 not in changes or changes[10] == 0:
                    break
                changes[10] -= 1
                change -= 10

            while change >= 5:
                if 5 not in changes or changes[5] == 0:
                    break
                changes[5] -= 1
                change -= 5

            if change > 0:
                return False

            if cost not in changes:
                changes[cost] = 0
            changes[cost] += 1

        return True

solution = Solution()
print(solution.lemonadeChange([5, 5, 5, 10, 20]) == True)
print(solution.lemonadeChange([5, 5, 10, 10, 20]) == False)