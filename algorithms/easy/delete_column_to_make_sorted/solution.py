class Solution:
    def minDeletionSize(self, strs: list) -> int:
        count = 0

        for i in range(0, len(strs[0])):
            column, orders = "", []
            for j in range(0, len(strs)):
                column += strs[j][i]
                orders.append(strs[j][i])

            orders.sort()
            sorted_column = "".join(orders)

            if sorted_column != column:
                count += 1

        return count

solution = Solution()
print(solution.minDeletionSize(["cba", "daf", "ghi"]) == 1)
print(solution.minDeletionSize(["a", "b"]) == 0)
print(solution.minDeletionSize(["zyx", "wvu", "tsr"]) == 3)