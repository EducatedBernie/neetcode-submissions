# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        c1 = list1
        c2 = list2
        dummy = ListNode(-1, None)
        originalHead = dummy
        while c1 and c2:
            if c1.val <= c2.val:
                print("c1 ", c1.val, " c2 ", c2.val)
                print("attach c1 not c2")
                dummy.next = c1
                dummy = dummy.next
                c1 = c1.next
                
            
            elif c2.val < c1.val:
                print("c1 ", c1.val, " c2 ", c2.val)
                print("attach c2 not c1")
                dummy.next = c2
                dummy = dummy.next
                c2 = c2.next
                
            
        if c1: 
            dummy.next = c1
        elif c2:
            dummy.next = c2
        else:
            dummy.next = None

        return originalHead.next