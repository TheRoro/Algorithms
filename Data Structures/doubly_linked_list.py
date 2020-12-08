class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tails = None
        self.length = 0

    def size(self):
        return self.length

    def append(self, data):
        node = Node(data)

        if(self.size() == 0):
            self.head = node
        elif(self.size() == 1):
            self.tails = node
            self.head.next = self.tails
            self.tails.prev = self.head
        else:
            self.tails.next = node
            node.prev = self.tails
            self.tails = node
        self.length+=1


listy = DoublyLinkedList()

print(listy.length)
listy.append("RORO")
listy.append("CHINO")
print(listy.head.next.data)
print(listy.tails.prev.data)
listy.append("JUANKA")
listy.append("LEYVA")
print(listy.tails.data)
print(listy.tails.prev.data)
print(listy.length)