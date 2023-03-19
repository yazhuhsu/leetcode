class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        done = 0
        for i in range(m+n):
            for j in range(n):
                if nums2[j] == 'done':
                    continue
                if nums2[j] < nums1[i]:
                    nums1[i+1:]=nums1[i:len(nums1)-1]
                    nums1[i] = nums2[j]
                    nums2[j] = 'done'
                    done+=1
                    break

                if i >= m+done and nums1[i] == 0:
                    nums1[i] = nums2[j]
                    nums2[j] = 'done'
                    done +=1