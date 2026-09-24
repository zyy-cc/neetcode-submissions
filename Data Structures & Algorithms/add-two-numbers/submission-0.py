# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
    
        while l1 and l2:
            sum2 = l1.val + l2.val + carry
            if sum2 <= 9:
                carry = 0
            else:
                carry = 1
            Node = ListNode(sum2%10)
            cur.next = Node
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + carry
            Node = ListNode(val % 10)
            carry = val // 10
            cur.next = Node
            cur = cur.next
            l1 = l1.next
        while l2:
            val = l2.val + carry
            Node = ListNode(val % 10)
            carry = val // 10
            cur.next = Node
            cur = cur.next
            l2 = l2.next
        if carry == 1:
            Node = ListNode(1)
            cur.next = Node

        return dummy.next
        
        
        