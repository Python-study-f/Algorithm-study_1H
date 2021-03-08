# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/add-two-numbers/
# 60 ms	14.2 MB
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = node = ListNode()
        carry = 0
        
        while l1 or l2 or up:
            # 리스트의 수가 다른경우 에러방지
            num1 = 0
            num2 = 0
            if l1:
                num1 = l1.val
            if l2:
                num2 = l2.val
                
            # 계산
            sumVal = num1 + num2 + carry
            carry = 0
            node.next = ListNode(sumVal % 10)
            
            # 자리올림
            if sumVal >= 10:
                carry = 1
                
            # 다음 노드로
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return root.next
            