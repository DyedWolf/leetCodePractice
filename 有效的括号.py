"""
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

示例 1：
输入：s = "()"
输出：true

示例2：
输入：s = "()[]{}"
输出：true

示例3：
输入：s = "(]"
输出：false

"""


class Solution(object):
    def is_valid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack


if __name__ == "__main__":
    solution = Solution()
    print(solution.is_valid("{{}}"))

