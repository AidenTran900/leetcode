# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        if head.next == None:
            return head

        def recurse(prev, cur):
            if cur == None:
                return prev
                
            new = recurse(cur, cur.next)

            prev.next = None
            cur.next = prev

            # print(str(prev.val) + " <- " + str(cur.val))
            return new

        return recurse(head, head.next)