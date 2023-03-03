"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

"""


# 找到数组中最小的值 print(min([6, 4, 6])) -> 4

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        same_str = ""
        string1, count = strs[0], len(strs)
        for i in range(1, count):
            same_str = self.judge_string(string1, strs[i])
            if not same_str:
                return ""
        print(type(same_str))
        return same_str

    def judge_string(self, string1, string2):
        same_string = ""
        length = min(len(string1), len(string2))
        for i in range(length):
            if string1[i] == string2[i]:
                same_string += string1[i]
            else:
                break
        return same_string


if __name__ == "__main__":
    strs = ["dog", "racecar", "car"]
    s = Solution()
    print(s.longestCommonPrefix(strs))
