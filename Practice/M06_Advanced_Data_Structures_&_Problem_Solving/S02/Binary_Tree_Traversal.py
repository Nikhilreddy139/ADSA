from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create Binary Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def bfs(node):

    # Base case
    if node is None:
        return

    queue = deque()

    queue.append(node)

    while queue:
        current = queue.popleft()

        print(current.data, end=" ")

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

print("BFS Traversal:")
bfs(root)