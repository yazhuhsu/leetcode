class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersections = []
        for num in nums1:
            if num in nums2:
                intersections.append(num)
                nums2.remove(num)

        return intersections