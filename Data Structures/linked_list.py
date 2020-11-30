class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printy(self):
        val = self.head
        while val != None:
            print(val.data)
            val = val.next


listy = LinkedList()
listy.head = Node(1)
second = Node(2)
third = Node(3)
listy.head.next = second
second.next = third
listy.printy()
