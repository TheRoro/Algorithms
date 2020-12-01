class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tails = None
        self.length = 0

    def printy(self):
        val = self.head
        while val != None:
            print(val.data)
            val = val.next
    
    def append(self, node):
        val = self.head
        while val.next != None:
            val = val.next
        val.next = node
        self.length+=1
    
    def size(self):
        return self.length

    def appendy(self, node):
        if(self.size() == 0):
            self.head = node
        elif(self.size() == 1):
            self.tails = node
            self.head.next = self.tails
        else:
            self.tails.next = node
            self.tails = node
        self.length+=1


listy = LinkedList()

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)

listy.appendy(one)
listy.appendy(two)
listy.appendy(three)
listy.appendy(four)


listy.printy()
print(listy.size())