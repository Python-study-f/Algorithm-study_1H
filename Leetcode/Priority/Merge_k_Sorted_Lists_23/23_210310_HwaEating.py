class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        mn = 1e5
        arr = []
        for i in lists:
            while i:
                arr.append(i.val)
                i = i.next
        arr.sort()
        if not arr:
            return ListNode('')
        
        ans = ListNode()
        cur = ans
        for i in range(len(arr)):
            cur.val = arr[i]
            if i == len(arr)-1:
                continue
            else:
                cur.next = ListNode()
            cur = cur.next
        
        return ans
        