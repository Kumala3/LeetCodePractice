# Link to the problem: https://leetcode.com/problems/remove-element/

class Solution:
    """
    Class representing a solution to the 'removeElement' problem.
    
    The 'removeElement' method removes all instances of a given value from a list of integers.
    It modifies the input list in-place and returns the new length of the list after removal.
    """
    def removeElement(self, nums: list[int], val: int) -> int:
        nums[:] = [d for d in nums if d != val]

        return len(nums)


sol = Solution()
print(sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 4))
