# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        head = ListNode()
        answer = head

        st = []

        if lists is None:
            return

        for i in range(len(lists)):
            while lists[i] is not None:
                st.append(lists[i].val)
                lists[i] = lists[i].next

        if len(st) == 0:
            return

        st.sort()
        answer.val = st[0]
        for i in range(1, len(st)):
            answer.next = ListNode(st[i])
            answer = answer.next

        return head