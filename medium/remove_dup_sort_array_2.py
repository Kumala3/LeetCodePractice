# Link to the problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        k = 1
        j = 1

        for i in range(1, len(nums)):
        
        # If current number equals to the previous number
            if nums[i] == nums[i - 1]:
                k += 1
            else:
                k = 1

            if k <= 2:
                nums[j] = nums[i]
                j += 1
        return j


sol = Solution()
print(sol.removeDuplicates([0, 1, 1, 2, 3, 3]))  # 7
