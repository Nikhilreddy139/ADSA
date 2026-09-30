#Queue Implementation using Linked List
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        item = self.front.val
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        return item

    def is_empty(self):
        return self.front is None
    def frontp(self):
        if not self.is_empty():
            return self.front.val
        else:
            return "Queue is empty"

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        while current:
            print(current.val, end=" ")
            current = current.next
        print()
s = LinkedListQueue()
print(s.dequeue())
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)
print(s.size())
print(s.dequeue())
print(s.dequeue())
s.display()