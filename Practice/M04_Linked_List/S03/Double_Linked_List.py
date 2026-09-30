'''
Double Linked List :
The data can be store in the nodes
Nodes --> 3 parts 
1. data 
2. prev
3. Next  
Algorithm :
1. Create node
2. insert data
3. connection
4. traverse    

class Node:
    def __init__(self,data):
        self.data = data 
        self.prev = None 
        self.next = None 
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2 
node2.prev = node1

node2.next = node3 
node3.prev = node2 

node3.next = node4 
node4.prev = node3 

def traverse():
    curr = node1 
    while curr:
        print(curr.data, end = " <-> ")
        curr = curr.next 
    print("None")
traverse()


def traverse():
    curr = node4 
    while curr:
        print(curr.data, end = " <-> ")
        curr = curr.prev 
    print("None")
traverse()
'''
#Insertion of a node at the beginning:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
def insert_begin(head, data):
    new_node = Node(data)
    new_node.next = head 
    if head is not None:
        head.prev = new_node
    return new_node 

def insert_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node 
    curr = head 
    while curr.next:
        curr = curr.next 
    curr.next = new_node 
    new_node.prev = curr 
    return head

def traverse(head):
    curr = head 
    while curr:
        print(curr.data, end = " <-> ")
        curr = curr.next 
    print("None")
head = None 
head = insert_begin(head, 50)
head = insert_begin(head, 60)
head = insert_begin(head, 70)
print("Insertion at the bring")
traverse(insert_begin(head, 80))
print()

print("Insertion at the end")
traverse(insert_end(head, 40))
print()