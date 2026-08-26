# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        if head.next == None:
            return False

        def recurse(slow, fast):
            if slow.next == None: # If there are no cycles, there will always be a leaf node
                return False
            if fast.next == None:
                return False
            if fast.next.next == None:
                return False

            if slow == fast:
                return True

            return recurse(slow.next, fast.next.next)

        return recurse(head, head.next) 