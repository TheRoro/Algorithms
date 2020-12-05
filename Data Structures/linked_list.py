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
    
    def dumb_append(self, node):
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
    
    def findy(self, find_node):
        val = self.head
        i = 0
        while val.next != None and val.data != find_node:
            val = val.next
            i+=1
        
        if(val.data == find_node):
            return i
        else:
            return False

    def getty(self, pos):
        if type(pos) is not int:
            return "Wrong type :("
        if pos >= self.length or pos < 0: #add typeof int only
            return False
        val = self.head
        i = 0
        while val.next != None and i != pos:
            val = val.next
            i+=1
        
        return val.data



listy = LinkedList()

one = Node("RORO")
two = Node("CHINO")
three = Node("JUANKA")
four = Node("LEYVA")

listy.appendy(one)
listy.appendy(two)
listy.appendy(three)
listy.appendy(four)

print("List elements are:")
listy.printy()

print("List size is:")
print(listy.size())

print("Element is at index:")
print(listy.findy("LEYVA"))

for i in range(listy.size()):
    print(listy.getty(i))
