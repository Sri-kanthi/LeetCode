class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        prev = dummy
        curr = dummy.next

        while curr and curr.next:
            nxt = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = nxt
            prev.next = second

            prev = curr
            curr = nxt

        return dummy.next