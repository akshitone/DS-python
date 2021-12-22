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

    # node is a TreeNode object
    def tree_to_tuple(self):

        # if node is None
        if self is None:
            return None

        # if node has no children
        if self.left is None and self.right is None:
            # return the key of the node
            return self.key

        # return the left child, the node, and the right child
        return TreeNode.tree_to_tuple(self.left),  self.key, TreeNode.tree_to_tuple(self.right)

    # space is used for spacing, node is the root node, level is the current level
    def display_keys(self, space="\t", level=0):
        if self is None:
            # print empty node
            print(space*level + "∅")
            return

        # if node has no children
        if self.left is None and self.right is None:
            # print the key of the node
            print(space*level + str(self.key))
            return

        # call the function recursively for the left child
        TreeNode.display_keys(self.left, space, level+1)
        # print the key of the node
        print(space*level + str(self.key))
        # call the function recursively for the right child
        TreeNode.display_keys(self.right, space, level+1)

    def traverse_in_order(self):
        if self is None:
            return []

        # creating a list to store the keys - in order traversal
        return TreeNode.traverse_in_order(self.left) + [self.key] + TreeNode.traverse_in_order(self.right)

        # pre order traversal
        # return [node.key] + TreeNode.traverse_in_order(node.left) + TreeNode.traverse_in_order(node.right)
        # post order traversal
        # return TreeNode.traverse_in_order(node.left) + TreeNode.traverse_in_order(node.right) + [node.key]

    def tree_height(self):
        if self is None:
            return 0

        return 1 + max(TreeNode.tree_height(self.left), TreeNode.tree_height(self.right))

    def tree_size(self):
        if self is None:
            return 0

        return 1 + TreeNode.tree_size(self.left) + TreeNode.tree_size(self.right)

    def __repr__(self):
        return "BinaryTree <{}>".format(self.tree_to_tuple())

    def __str__(self):
        return self.__repr__()


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

    # TreeNode.display_keys(tree, "    ")

    print(TreeNode.traverse_in_order(tree))
