class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        positions = {}
        for idx, num in enumerate(nums):
            positions.setdefault(num, [])
            positions[num].append(idx)

        for num, pos in positions.items():
            if len(pos) < 2:
                continue

            for idx, p_i in enumerate(pos):
                for p_j in pos[idx:]:
                    if p_i == p_j:
                        continue
                    if p_j - p_i <= k:
                        return True


        return False