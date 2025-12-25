class Solution:
    def minimumBoxes(self, apple: list, capacity: list) -> int:
        capacity.sort(reverse=True)

        sum, boxes = 0, 0
        for _, a in enumerate(apple):
            sum += a

        for _, cap in enumerate(capacity):
            if sum >= cap:
                sum -= cap
                boxes += 1
                continue

            if sum > 0:
                boxes += 1

            break

        return boxes

solution = Solution()
print(solution.minimumBoxes([1, 3, 2], [4, 3, 1, 5, 2]) == 2)
print(solution.minimumBoxes([5, 5, 5], [2, 4, 2, 7]) == 4)