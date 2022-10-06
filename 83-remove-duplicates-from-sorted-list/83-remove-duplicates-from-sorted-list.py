# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while (current != None) :
            # if next value didn't change
            
            while (current.next != None and current.val == current.next.val) :
                #skip next node
                current.next = current.next.next
            current = current.next
        return head
    