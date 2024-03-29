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

    def print(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def append(self, data):
        node = Node(data)

        if self.size() == 0:
            self.head = node
        elif self.size() == 1:
            self.tails = node
            self.head.next = self.tails
            self.tails.prev = self.head
        else:
            self.tails.next = node
            node.prev = self.tails
            self.tails = node
        self.length += 1

    def push(self, data):
        node = Node(data)

        if self.size() == 0:
            self.head = node
        elif self.size() == 1:
            self.tails = self.head
            self.head = node
            self.head.next = self.tails
            self.tails.prev = self.head
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_at(self, data, pos):
        if type(pos) is not int:
            return "Not a valid position"
        elif pos < 0 or pos > self.length:
            return False

        if pos == 0:
            self.push(data)
            # print("I'm a push")
        elif pos == self.length:
            self.append(data)
            # print("I'm an append")
        else:
            node = Node(data)
            # since I have 2 pointers I should start with the closest
            diff1 = abs(0 - pos)
            diff2 = abs(self.length - pos)

            if diff1 > diff2:
                # Position closer to the end (so I use the prev pointer)
                temp1 = self.tails
                temp2 = self.tails
                i = self.length
                while temp2.prev is not None and i != pos:
                    temp1 = temp2
                    temp2 = temp2.prev
                    i -= 1
                # print("I'm closer to the end")
                temp1.prev = node
                node.next = temp1
                temp2.next = node
                node.prev = temp2
                self.length += 1
            else:
                # Position closer to the start or same length (so I use the next pointer)
                temp1 = self.head
                temp2 = self.head
                i = 0
                while temp2.next is not None and i != pos:
                    temp1 = temp2
                    temp2 = temp2.next
                    i += 1
                # print("I'm closer to the start")
                temp1.next = node
                node.prev = temp1
                node.next = temp2
                temp2.prev = node
                self.length += 1

    def reverse(self):
        first = None
        second = self.head
        third = self.head.next

        self.tails = second

        while second is not None:
            second.next = first
            second.prev = third
            first = second
            second = third
            if third is not None:
                third = third.next

        self.head = first


_list = DoublyLinkedList()

print(_list.length)
_list.insert_at("John", 0)
_list.insert_at("Mark", 1)
_list.insert_at("Bob", 1)
_list.insert_at("Steve", 2)

_list.print()
_list.reverse()
print("Reversed doubly linked list")
_list.print()

print(_list.length)
