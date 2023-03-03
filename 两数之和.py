"""

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

"""
from typing import List


class Solution1:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()  #
        for i, num in enumerate(nums):  # [(0, 11),(1, 7),(2, 15),(3, 2)]
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i   # {11: 0, 7: 1, 15: 2}
        return []

    def try_try(self):
        hashtable = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
        if "key1" in hashtable:
            print(True)
        else:
            print(False)

        dataList = ["value1", "value2", "value3", "value4"]
        if "value1" in dataList:
            print(True)
        else:
            print(False)


"""
[-2, {11: 0}]
[2, {11: 0, 7: 1}]
[-6, {11: 0, 7: 1, 15: 2}]
[7, {11: 0, 7: 1, 15: 2, 2: 3}]
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums) - 1):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    print(x, y)
                    return [x, y]


if __name__ == "__main__":
    nums = [11, 7, 15, 2]
    target = 9
    s = Solution1()
    s.twoSum1(nums, target)
    print(s.twoSum1(nums, target))
    s.try_try()
