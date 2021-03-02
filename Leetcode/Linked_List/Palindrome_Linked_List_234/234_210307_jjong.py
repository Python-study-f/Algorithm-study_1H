# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        st = []

        while head is not None:
            val = head.val
            st.append(val)
            head = head.next

        if st == st[::-1]:
            return True
        else:
            return False
