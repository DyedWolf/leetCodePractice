"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。
 

示例 1：

输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。

"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        len_x = int(len(str(x)))
        aa = str(x)[0:int(len_x / 2)]
        bb = str(x)[int(len_x) - int(len_x // 2):int(len_x)]
        if aa == bb[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    x = -12321
    s = Solution()
    print(s.isPalindrome(x))
