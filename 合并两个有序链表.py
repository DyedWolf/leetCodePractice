"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]

"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# class Solution(object):
#     def mergeTwoLists(self, list1, list2):  # [1,2] [3,4]
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         result_list = []
#         all_list = list2 + list1
#         # for i, num in enumerate(all_list):
#         for i in range(len(all_list)):
#             min_num = min(all_list)
#             result_list.append(min_num)
#             all_list.remove(min_num)
#         print(result_list)


if __name__ == "__main__":
    l = ListNode()
    solution = Solution()

    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    solution.mergeTwoLists(ListNode(list1), ListNode(list2))
