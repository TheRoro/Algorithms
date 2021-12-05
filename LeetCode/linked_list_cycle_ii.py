class Solution(object):
    def detectCycle(self, head):
        dicty = {}
        if head == None or head.next == None:
            return None
        while head != None:
            if head not in dicty:
                dicty[head] = 1
            else:
                return head
            head = head.next
        return None