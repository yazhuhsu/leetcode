class Solution:
    def findXSum(self, nums: list, k: int, x: int) -> list:
        sums = []
        for idx in range(0, len(nums)-k+1):
            sub_nums = nums[idx:idx+k]
            count_dict = dict()
            for sub_idx in range(0, len(sub_nums)):
                if sub_nums[sub_idx] not in count_dict:
                    count_dict[sub_nums[sub_idx]] = 0
                count_dict[sub_nums[sub_idx]]+=1

            counts = sorted(count_dict.items(), key=lambda item: (-item[1], -item[0]))

            sums.append(0)
            if len(dict(counts)) < x:
                for key, value in dict(counts).items():
                    sums[idx] += key*value
                continue

            done = 0
            for key, value in dict(counts).items():
                sums[idx] += key*value
                done += 1
                if done == x:
                    break

        return sums

print(Solution().findXSum([1, 1, 2, 2, 3, 4, 2, 3], 6, 2) == [6, 10, 12])
print(Solution().findXSum([3, 8, 7, 8, 7, 5], 2, 2) == [11, 15, 15, 15, 12])