class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        # Removing the head
        if n == len(nodes):
            return head.next

        # Node before the node to remove
        prev = nodes[-(n + 1)]

        # Skip the node to remove
        prev.next = prev.next.next

        return head