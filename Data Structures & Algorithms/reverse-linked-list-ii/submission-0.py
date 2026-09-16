class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy
        
        # Step 1: move `prev` to the node just before position `left`
        for _ in range(left - 1):
            prev = prev.next
        
        # `curr` is the first node of the sublist to reverse (will end up last after reversal)
        curr = prev.next
        
        # Step 2: reverse the sublist by repeatedly moving curr.next to the front
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        return dummy.next
        