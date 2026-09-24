# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle point
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        left_head, right_head = head, slow.next
        slow.next = None

        # reverse the right side
        prev = None
        cur = right_head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        right_head = prev
        
        # merge the two list 
        while right_head:
            left_next = left_head.next
            right_next = right_head.next
            left_head.next = right_head
            right_head.next = left_next
            left_head = left_next
            right_head = right_next
        


        


        