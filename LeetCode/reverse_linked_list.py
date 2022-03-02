class Solution:
    def reverseList(self, head):
        prev = None
        actual = head
        while actual:
            nextnode = actual.next
            actual.next = prev
            prev = actual
            actual = nextnode

        return prev
