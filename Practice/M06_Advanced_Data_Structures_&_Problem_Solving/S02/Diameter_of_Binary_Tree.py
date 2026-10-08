class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


def diameter(root):
    result = [0]
    def height(node):
        if node is None:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)

        current_diameter = left_height + right_height

        result[0] = max(result[0], current_diameter)

        return 1 + max(left_height, right_height)
    height(root)
    return result[0]

print("Diameter of tree:", diameter(root))

'''
Problems:
100
101
104
111
110
'''