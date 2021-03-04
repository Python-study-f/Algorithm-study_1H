# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/swap-nodes-in-pairs/submissions/
# 40 ms	14.4 MB
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        while head and head.next:
            tmpNode = head.next
            head.next = self.swapPairs(tmpNode.next)
            tmpNode.next = head
            return tmpNode
        # 노드가 홀수개
        return head