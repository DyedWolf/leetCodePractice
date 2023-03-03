"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

 

示例 1:

输入: nums = [1,3,5,6], target = 5
输出: 2
示例 2:

输入: nums = [1,3,5,6], target = 2
输出: 1
示例 3:

输入: nums = [1,3,5,6], target = 7
输出: 4

"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        new_nums = []
        for i, num in enumerate(nums):
            if num == target:
                print(i)
                return i
            elif num < target and nums[i + 1] > target:
                new_nums.append(num)
                print(i)
                return i + 1
            elif nums[-1] < target:
                print(len(nums))
                return len(nums)
            elif num > target:
                print(i)
                return i


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 0
    solution = Solution()
    solution.searchInsert(nums, target)
