class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_distance, y_distance = x-z, y-z

        if x_distance < 0:
            x_distance = -x_distance
        if y_distance < 0:
            y_distance = -y_distance

        if x_distance > y_distance:
            return 2
        elif x_distance < y_distance:
            return 1

        return 0

cases = [
    [2, 7, 4],
    [2, 5, 6],
    [1, 5, 3]
]

answers = [1, 2, 0]

solution = Solution()
for idx, v in enumerate(cases):
    answer = solution.findClosest(v[0],v[1],v[2])
    if answer != answers[idx]:
        print(f'n={v} Wrong!')
        print(f'output:{v}, answer:{answers}')
        break

    print(f'n={v} Correct!')