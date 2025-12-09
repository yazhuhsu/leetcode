class Solution:
    def specialTriplets(self, nums: list) -> int:
        mod = 10**9 + 7
        num_dict = dict()

        for i in range(len(nums)):
            if nums[i] not in num_dict:
                num_dict[nums[i]] = []

            num_dict[nums[i]].append(i)

        if len(num_dict) == 1:
            if 0 in num_dict:
                count = int((len(nums) - 2) * (len(nums) - 1) * len(nums) / 6)
                return count % mod
            else:
                return 0

        count = 0
        for key, value in num_dict.items():
            twice = key * 2
            if twice not in num_dict:
                continue

            twice_nums = num_dict[twice]
            for _, v in enumerate(value):
                idx = binarySearch(twice_nums, v)
                if key == twice:
                    count += (idx - 1) * (len(twice_nums) - idx)
                else:
                    count += idx * (len(twice_nums) - idx)

        return count % mod


def binarySearch(nums: list, key: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if nums[mid] > key:
            end = mid - 1
        else:
            start = mid + 1

    return start

solution = Solution()
print(solution.specialTriplets([6,3,6])==1)
print(solution.specialTriplets([0, 1, 0, 0])==1)
print(solution.specialTriplets([8, 4, 2, 8, 4])==2)