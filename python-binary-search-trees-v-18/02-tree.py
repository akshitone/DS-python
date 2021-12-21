# Node class
class TreeNode:

    # Constructor
    def __init__(self, key):
        # Key of the node
        self.key = key
        # Left child
        self.left = None
        # Right child
        self.right = None

    # Static method to create a tree
    @staticmethod
    # Parse a list of tuple to a tree
    def parse_tuple(data):
        # print(data)

        # Check if the data is a tuple and has 3 elements
        if isinstance(data, tuple) and len(data) == 3:
            # Create a node
            node = TreeNode(data[1])
            # Set the left child
            node.left = TreeNode.parse_tuple(data[0])
            # Set the right child
            node.right = TreeNode.parse_tuple(data[2])

        # Check if the data is None
        elif data is None:
            node = None

        else:
            # Create a node
            node = TreeNode(data)

        return node

    @staticmethod
    def tree_to_tuple(node):
        if node is None:
            return None
        if node.left is None and node.right is None:
            return node.key
        return TreeNode.tree_to_tuple(node.left),  node.key, TreeNode.tree_to_tuple(node.right)

    @staticmethod
    def display_keys(node, space="\t", level=0):
        if node is None:
            print(space*level + "∅")
            return

        if node.left is None and node.right is None:
            print(space*level + str(node.key))
            return

        TreeNode.display_keys(node.left, space, level+1)
        print(space*level + str(node.key))
        TreeNode.display_keys(node.right, space, level+1)


if __name__ == "__main__":
    root = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    root.left = node4
    root.right = node5

    tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = TreeNode.parse_tuple(tree_tuple)

    tuple_from_tree = TreeNode.tree_to_tuple(tree)
    # print(tuple_from_tree)

    TreeNode.display_keys(tree, "    ")
