from typing import List

class Solution(object):

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 1
        output = [-1, -1]
        end = len(nums)
        for x in range(0, end):
            for y in range(x + 1, end):
                if (nums[x] + nums[y] == target):
                    return [x, y]
        return [0, 0]


solution = Solution()
print("Output", solution.twoSum([2, 7, 11, 15], 9))
print("Output", solution.twoSum([3, 2, 4], 6))
print("Output", solution.twoSum([3, 3], 6))
print("Output", solution.twoSum([1, 5, 9, 13, 22, 2, 7], 15))
