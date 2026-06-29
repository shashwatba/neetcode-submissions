# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if head is None:
            return head
        elif head.next is None:
            return head
        else:
            curr = prev.next
            next_node = curr
            prev.next = None
        while next_node is not None:
            if curr.next is not None:
                next_node = curr.next
            else:
                curr.next = prev
                break
            curr.next = prev
            prev = curr
            curr = next_node

        return curr
        
