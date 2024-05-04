class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Merge two sorted arrays nums1 and nums2 into nums1 in-place.

        Args:
            nums1 (List[int]): The first sorted array.
            m (int): The number of elements in nums1 (excluding the extra space allocated for nums2).
            nums2 (List[int]): The second sorted array.
            n (int): The number of elements in nums2.

        Returns:
            None: The function modifies nums1 in-place.
        """
        p1, p2 = m - 1, n - 1

        for p in range(m + n - 1, -1, -1):
            # If p2 is less than 0, it means that all elements from nums2 have been placed into nums1,
            # so the loop can break early.
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

sol = Solution()
sol.merge(nums1, m, nums2, n)

print(nums1)  # [1, 2, 2, 3, 5, 6]
