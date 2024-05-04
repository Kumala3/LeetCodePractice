# Link to the problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    """
    Class representing a solution to the problem of removing duplicates from a sorted array.
    """

    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Removes duplicates from the given sorted array and returns the length of the modified array.

        Args:
            nums (list[int]): The sorted array containing duplicates.

        Returns:
            int: The length of the modified array after removing duplicates.
        """
        j = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1

        return j


sol = Solution()
print(sol.removeDuplicates([1, 1, 2, 5, 6]))
