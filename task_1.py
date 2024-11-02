class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

def find_max(node):
    if node is None:
        return None
    current = node
    while current.right is not None:
        current = current.right
    return current.value

def main():
    root = None
    values = [20, 10, 5, 15, 30, 25, 35]
    for val in values:
        root = insert(root, val)

    max_value = find_max(root)
    print("The maximum value in the BST is:", max_value)

if __name__ == "__main__":
    main()
