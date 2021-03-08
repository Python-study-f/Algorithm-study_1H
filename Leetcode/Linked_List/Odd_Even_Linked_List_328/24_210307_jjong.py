# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head is not None:
            odd = head
            check = even = head.next

            while even and even.next:
                odd.next = even.next
                odd = odd.next
                even.next = odd.next
                even = even.next
            odd.next = check
            return head


'''
1. check는 odd값들을 잃지 않기 위해서 만든 list
2. 나머지는 앞선 문제랑 같음 
'''