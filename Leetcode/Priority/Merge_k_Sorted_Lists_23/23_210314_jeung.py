# Definition for singly-linked list.
import pdb
import numpy as np

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def mergeKLists(self, lists) -> ListNode:
#         merged = None
#         while lists:
#             tmp_list = []
#             for each_list in lists:
#                 tmp = each_list.val
#                 if tmp is not None:
#                     tmp_list.append(tmp)
#
#             index = np.argmin(tmp_list)
#             smallest = lists[index].val
#             lists[index] = lists[index].next
#
#             if merged is None:
#                 merged = ListNode(smallest)
#             else:
#                 merged.next = ListNode(smallest)
#                 merged = merged.next
#
#             lists = [each_list for each_list in lists if each_list is not None]
#
#         return merged

class Solution1:
    def mergeKLists(self, lists) -> ListNode:
        traversed = []
        head = point = ListNode(0)
        for each_list in lists:
            while each_list:
                traversed.append(each_list.val)
                each_list = each_list.next

        for i in sorted(traversed):
            point.next = ListNode(i)
            point = point.next

        return head.next


from queue import PriorityQueue

class Solution2(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        my_queue = PriorityQueue()
        for each_list in lists:
            if each_list:
                my_queue.put((each_list.val, each_list))

        while not my_queue.empty():
            val, node = my_queue.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                my_queue.put((node.val, node))
        return head.next
