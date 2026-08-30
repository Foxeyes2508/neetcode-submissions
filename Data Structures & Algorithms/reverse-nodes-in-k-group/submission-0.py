class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        grpPrev = dummy

        while True:

            kth = grpPrev

            for i in range(k):
                kth = kth.next

                if kth is None:
                    return dummy.next

            grpNext = kth.next

            prev = grpNext
            curr = grpPrev.next

            while curr != grpNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = grpPrev.next
            grpPrev.next = kth
            grpPrev = temp