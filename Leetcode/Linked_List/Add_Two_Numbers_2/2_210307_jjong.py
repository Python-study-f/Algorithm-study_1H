# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode()
        answer = head

        st1 = []
        st2 = []

        while l1 is not None:
            st1.append(str(l1.val))
            l1 = l1.next

        while l2 is not None:
            st2.append(str(l2.val))
            l2 = l2.next

        ans = list(str(int(''.join(st1[::-1])) + int(''.join(st2[::-1]))))
        ans.reverse()

        answer.val = int(ans[0])
        for i in range(1, len(ans)):
            answer.next = ListNode(int(ans[i]))
            answer = answer.next

        return head