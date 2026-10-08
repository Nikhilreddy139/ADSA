class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def Height(root):
    if root is None:
        return -1

    left_height = Height(root.left)
    right_height = Height(root.right)
    return 1 + max(left_height, right_height)

print("Height of tree:", Height(root))
def is_balanced(root):
    if root is None:
        return True

    left_height = Height(root.left)
    right_height = Height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return is_balanced(root.left) and is_balanced(root.right)

print("Is the tree balanced?", is_balanced(root))
print("Height of tree:", Height(root))