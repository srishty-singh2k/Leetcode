# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #TC=O(n) SC=O(1) with dummy
        # if not head or not head.next:
        #     return head
        # left = ListNode()
        # left.next=head
        # right = head
        # head=head.next
        # while(right and right.next):
        #     left.next = right.next
        #     right.next = right.next.next
        #     left.next.next = right
        #     left=right
        #     right=left.next
        # return head

        #TC=O(n) SCO(1) without dummy
        if not head or not head.next:
            return head
        left = head
        head = head.next
        left.next = left.next.next
        head.next = left
        right = left.next
        while(right and right.next):
            left.next = right.next
            right.next = right.next.next
            left.next.next = right
            left=right
            right=left.next
        return head
            

