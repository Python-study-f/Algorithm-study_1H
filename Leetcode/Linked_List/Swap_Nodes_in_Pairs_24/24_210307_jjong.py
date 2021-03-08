# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        ret = prev = ListNode()
        prev.next = head

        if head is None:
            return

        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head

            prev.next = tmp
            prev = prev.next.next

            head = head.next

        return ret.next

'''
1. stack 만들어서 홀 짝 나누면서 해도 되지만, 다른 문제들 다 이렇게 풀어서 이번엔 자료구조적인 부분에서 문제를 풀어봄
2. Linked List는 자료구조에서 가장 중요한 개념이기도 하기에 꼭 알아두고 가는 것이 중요
3. prev = prev.next.next를 하는 이유는 head가 옮겨가며 앞에 데이터 유실을 막기 위한 ListNode를 생성
'''