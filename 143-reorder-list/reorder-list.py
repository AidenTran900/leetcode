# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # recurse thru LL
        # map ind
        ind_map = {}

        def recurse(i, cur):
            if not cur:
                return 0
            ind_map[i] = cur

            return recurse(i + 1, cur.next) + 1
        
        n = recurse(0, head)
        
        for left in range(0, n//2):
            right = n - left - 1
            
            l_node = ind_map[left]
            r_node = ind_map[right]
            r_parent = ind_map[right-1]

            if l_node == r_parent:
                break

            l_child = l_node.next
            r_parent.next = None
            l_node.next = r_node
            r_node.next = l_child
