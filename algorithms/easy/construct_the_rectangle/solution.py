class Solution:
    def constructRectangle(self, area: int) -> list:
        w, l, diff = 0, 0, area
        for i in range(1, area+1):
            if area % i != 0:
                continue

            j = int(area / i)
            if j-i >= 0 and j-i <= diff:
                l = j
                w = i
                diff = j - i

        return [l, w]

solution = Solution()
print(solution.constructRectangle(37)==[37,1])
print(solution.constructRectangle(122122)==[427, 286])
print(solution.constructRectangle(1)==[1,1])