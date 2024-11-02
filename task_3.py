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

def sum_tree(node):
    if node is None:
        return 0
    return sum_tree(node.left) + node.value + sum_tree(node.right)

def main():
    root = None
    values = [20, 10, 5, 15, 30, 25, 35]
    for val in values:
        root = insert(root, val)

    total_sum = sum_tree(root)
    print("The sum of all values in the BST is:", total_sum)

if __name__ == "__main__":
    main()
