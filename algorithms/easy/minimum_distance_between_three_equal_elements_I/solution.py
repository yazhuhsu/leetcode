class Solution:
    def minimumDistance(self, nums: list) -> int:
        goods = {}
        for idx, num in enumerate(nums):
            if num not in goods:
                goods[num] = []
            
            goods[num].append(idx)

        distance = -1
        for _, good in goods.items():
            if len(good) < 3:
                continue

            for idx in range(len(good)-2):
                d = (good[idx+1]-good[idx]) + (good[idx+2]-good[idx+1]) + (good[idx+2]-good[idx])
                
                if distance != -1 and d > distance:
                    continue

                distance = d

        return distance

solution = Solution()
# Walkthrough example: two qualifying values, value 2 wins
print(solution.minimumDistance([1, 2, 1, 2, 2, 1]) == 6)
# Value 1 has 4 occurrences, best window [2,5,6] gives 8; value 2 still wins with 6
print(solution.minimumDistance([1, 2, 1, 2, 2, 1, 1]) == 6)
# Only one qualifying value
print(solution.minimumDistance([1, 2, 1, 3, 1]) == 8)
# No value appears 3 times
print(solution.minimumDistance([1, 2, 3]) == -1)
# All same value, best window is first three
print(solution.minimumDistance([1, 1, 1, 1]) == 4)
# Minimum possible distance (three consecutive equal elements)
print(solution.minimumDistance([5, 5, 5]) == 4)