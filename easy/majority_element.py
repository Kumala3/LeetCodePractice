# Link to the problem: https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Finds the majority element in the given array.

        Args:
            nums (list[int]): The array containing the majority element.

        Returns:
            int: The majority element in the given array.
        """
        nums.sort()  

        return nums[len(nums) // 2]


sol = Solution()
print(sol.majorityElement([3, 2, 3])) # 3
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2])) # 2
