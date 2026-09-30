'''
class Stack:
    def __init__(self):
        self.s = []

    def push(self, val):
        self.s.append(val)
    def is_empty(self):
        return len(self.s) == 0
    def pop(self):
        if not self.is_empty():
            return self.s.pop()
        else:
            return "Stack is empty"
    def size(self):
        return len(self.s)
    def peek(self):
        if not self.is_empty():
            return self.s[-1]
        else:
            return "Stack is empty"
    
st = Stack()
print(st.pop())
st.push(10)
st.push(20)
print(st.pop())
print(st.size())
print(st.peek())
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Stack_LL:
    def __init__(self):
        self.top = None
    def is_empty(self):
        return self.top is None
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if not self.is_empty():
            val = self.top.val
            self.top = self.top.next
            return val
        else:
            return "Stack is empty"
    def size(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    def peek(self):
        if not self.is_empty():
            return self.top.val
        else:
            return "Stack is empty"
    
st = Stack_LL()
print(st.pop())
print(st.is_empty())
st.push(10)
print(st.pop())
st.push(20)