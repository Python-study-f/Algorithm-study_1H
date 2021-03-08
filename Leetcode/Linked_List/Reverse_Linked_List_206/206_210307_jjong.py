# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, l1: ListNode) -> ListNode:

        head = ListNode()
        answer = head
        st = []

        if l1 is None:
            return

        while l1 is not None:
            st.append(l1.val)
            l1 = l1.next

        st.reverse()

        answer.val = st[0]

        for i in range(1, len(st)):
            answer.next = ListNode(st[i])
            answer = answer.next

        return head