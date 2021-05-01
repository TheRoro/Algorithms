class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tails = None
        self.length = 0
    
    def size(self):
        return self.length

    def enqueue(self, data):
        node = Node(data)

        if self.length == 0:
            self.head = node
        elif self.length == 1:
            self.tails = node
            self.head.next = self.tails
        else:
            self.tails.next = node
            self.tails = node

        self.length+=1

    def dequeue(self):
        if self.length == 0:
            return False
        else:
            val = self.head
            if self.length == 1:
                self.head = None
            elif self.length == 2:
                self.head = self.tails
                self.tails = None
            else:
                self.head = self.head.next
            self.length-=1
            return val.data


    def print(self):
        current = self.head

        while current != None:
            print(current.data)
            current = current.next
    
    def front(self):
        return self.head.data
    
    def back(self):
        return self.tails.data

queue = Queue()

print(queue.size())
queue.enqueue("Ro")
queue.enqueue("Chi")
queue.enqueue("Jua")
queue.enqueue("Ley")
print("My Queue is:")
queue.print()
print("Erasing elements:")
print(queue.dequeue())
print(queue.dequeue())
print("Final Queue is:")
queue.print()
print(queue.size())

print(queue.front())
print(queue.back())