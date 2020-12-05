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
        if pos >= self.length or pos < 0:
            return False
        val = self.head
        i = 0
        while val.next != None and i != pos:
            val = val.next
            i+=1
        
        return val.data

    def pop(self):
        if self.length == 0:
            return False
        val = self.head
        if(self.size() == 1):
            self.head = None
        elif(self.size() == 2):
            self.head = self.head.next
            self.tails = None
        else:
            self.head = self.head.next
        self.length-=1
        return val.data
    
    def pop_back(self):
        if self.length == 0:
            return False
        val = self.tails
        if(self.size() == 1):
            val = self.head
            self.head = None
        elif(self.size() == 2):
            self.head.next = None
            self.tails = None
        else:
            temp = self.head
            pos = self.length - 2
            i = 0
            while temp.next != None and i != pos:
                temp = temp.next
                i+=1
            temp.next = None
            self.tails = temp
        self.length-=1
        return val.data

    def deletyAt(self, pos):
        if type(pos) is not int:
            return "Wrong type :("
        if pos >= self.length or pos < 0:
            return False
        
        #Three cases:
        #Element is at first position, create pop method
        #Element is at last position, create pop_back method
        #Element is at the middle, so there is: First, Middle, Last
        #Remove pointer next from first and reasign to last
        
        if pos == 0: #First position
            self.pop()
        elif pos == self.length - 1: #last position
            print("entre aqui")
            self.pop_back()
        else:
            temp = self.head
            temp2 = self.head
            i = 0
            while temp2.next != None and i != pos:
                temp = temp2
                temp2 = temp2.next
                i+=1
            temp.next = temp2.next
            temp2.next = None
            self.length-=1
            #UPDATE TAILS
            return temp2.data

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

print("Element LEYVA is at index:")
print(listy.findy("LEYVA"))

print("Element at index 1 is:")
print(listy.getty(1))

# print("deleting first element....")
# print(listy.pop())

# print("List size is:")
# print(listy.size())

# print("List elements are:")
# listy.printy()

# print("deleting last element....")
# print(listy.pop_back())

# print("List size is:")
# print(listy.size())

# print("List elements are:")
# listy.printy()

print("Erasing element at position 1:")
print(listy.deletyAt(1))

print("List size is:")
print(listy.size())

print("List elements are:")
listy.printy()

print("Erasing element at position 1:")
print(listy.deletyAt(1))

print("List size is:")
print(listy.size())

print("List elements are:")
listy.printy()

print("Erasing element at position 1:")
print(listy.deletyAt(1))

print("List size is:")
print(listy.size())

print("List elements are:")
listy.printy()

print("Erasing element at position 1:")
print(listy.deletyAt(1))

print("List size is:")
print(listy.size())

print("List elements are:")
listy.printy()