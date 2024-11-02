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

def find_min(node):
    if node is None:
        return None
    current = node
    while current.left is not None:
        current = current.left
    return current.value

def main():
    root = None
    values = [20, 10, 5, 15, 30, 25, 35]
    for val in values:
        root = insert(root, val)

    min_value = find_min(root)
    print("The minimum value in the BST is:", min_value)

if __name__ == "__main__":
    main()
