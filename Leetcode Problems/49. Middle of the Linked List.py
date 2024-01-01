# https://leetcode.com/problems/middle-of-the-linked-list/
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = []
        while head:
            x.append(head)
            head = getattr(head, 'next', None)
        return x[len(x)//2]
