# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode()
        answer = head

        if l1 is None and l2 is None:
            return

        sort_st = []

        while l1 is not None:
            sort_st.append(l1.val)
            l1 = l1.next

        while l2 is not None:
            sort_st.append(l2.val)
            l2 = l2.next

        sort_st.sort()
        answer.val = sort_st[0]
        for i in range(1, len(sort_st)):
            answer.next = ListNode(sort_st[i])
            answer = answer.next

        return head