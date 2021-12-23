class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return "User({}, {}, {})".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()


class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, key, value=None):
        if self is None:
            # if self is None, then create a new root node
            self = BSTNode(key, value)

        # if key is less than the current node's key
        elif key < self.key:
            # recursively insert into the left subtree
            self.left = BSTNode.insert(self.left, key, value)
            # set the parent of the left node to the current node
            self.left.parent = self

        # if key is greater than the current node's key
        elif key > self.key:
            # recursively insert into the right subtree
            self.right = BSTNode.insert(self.right, key, value)
            # set the parent of the right node to the current node
            self.right.parent = self

        return self

    def update_value(self, key, value):
        target = self.find_value(key)
        if target is not None:
            target.value = value

    def find_value(self, key):
        if self is None:
            return None

        # found the key
        elif key == self.key:
            return self

        # search the left subtree
        elif key < self.key:
            return BSTNode.find_value(self.left, key)

        # search the right subtree
        else:
            return BSTNode.find_value(self.right, key)

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
        BSTNode.display_keys(self.left, space, level+1)
        # print the key of the node
        print(space*level + str(self.key))
        # call the function recursively for the right child
        BSTNode.display_keys(self.right, space, level+1)

    def traverse_in_order(self):
        if self is None:
            return []

        # creating a list to store the keys - in order traversal
        return BSTNode.traverse_in_order(self.left) + [(self.key, self.value)] + BSTNode.traverse_in_order(self.right)

    def is_balanced(self):
        if self is None:
            return True, 0

        # left subtree
        left_balanced, left_height = BSTNode.is_balanced(self.left)
        # right subtree
        right_balanced, right_height = BSTNode.is_balanced(self.right)

        # check if the subtrees are balanced and the difference in height is less than or equal to 1
        balanced = left_balanced and right_balanced and (
            abs(left_height - right_height) <= 1)

        # return the height of the tallest subtree
        height = max(left_height, right_height) + 1

        return balanced, height

    def make_balanced_bst(users, low=0, high=None, parent=None):
        # it is the first call for root node
        if high is None:
            high = len(users) - 1

        if low > high:
            return None

        mid = (low + high) // 2
        # key is the username and value is the user object
        key, value = users[mid]

        # create a new node with the key and value
        root = BSTNode(key, value)
        # set the parent of the new node to the parent node
        root.parent = parent

        # create the left subtree
        root.left = BSTNode.make_balanced_bst(users, low, mid-1, root)
        # create the right subtree
        root.right = BSTNode.make_balanced_bst(users, mid+1, high, root)

        return root

    @staticmethod
    def balance_unbalanced_bst(node):
        return BSTNode.make_balanced_bst(BSTNode.traverse_in_order(node))


class TreeMap(BSTNode):
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = BSTNode.find_value(self.root, key)
        if not node:
            self.root = BSTNode.insert(self.root, key, value)
            self.root = BSTNode.balance_unbalanced_bst(self.root)
        else:
            BSTNode.update_value(self.root, key, value)

    def __getitem__(self, key):
        node = BSTNode.find_value(self.root, key)
        return node.value if node else None

    def __iter__(self):
        return (x for x in BSTNode.traverse_in_order(self.root))

    # def __len__(self):
    #     return tree_size(self.root)

    def display(self):
        return BSTNode.display_keys(self.root)


if __name__ == "__main__":
    john = User("john", "John Doe", "john@doe.com")
    aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
    biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
    hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
    jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
    siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
    sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
    vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

    users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

    # tree = BSTNode(jadhesh.username, jadhesh)
    # print(tree.key, tree.value)

    root = BSTNode.insert(None, jadhesh.username, jadhesh)
    root.insert(biraj.username, biraj)
    root.insert(sonaksh.username, sonaksh)
    root.insert(aakash.username, aakash)
    root.insert(hemanth.username, hemanth)
    root.insert(siddhant.username, siddhant)
    root.insert(vishal.username, vishal)

    # BSTNode.display_keys(root)

    # print(root.find_value('vishal').value)

    # updating_vishal = User('vishal', 'Vishal G', 'vishalg@example.com')
    # root.update_value('vishal', updating_vishal)

    # print(root.find_value('vishal').value)

    # print(root.traverse_in_order())

    # data = [(user.username, user) for user in users]

    # tree = BSTNode.make_balanced_bst(data)

    # tree2 = None
    # for user in users:
    #     tree2 = BSTNode.insert(tree2, user.username, user)

    # tree2.display_keys()

    # BSTNode.balance_unbalanced_bst(tree2).display_keys()

    treemap = TreeMap()

    # treemap.display()

    treemap['aakash'] = aakash
    treemap['jadhesh'] = jadhesh
    treemap['sonaksh'] = sonaksh
    treemap['vishal'] = vishal
    treemap['biraj'] = biraj
    treemap['hemanth'] = hemanth
    treemap['siddhant'] = siddhant

    # treemap.display()

    # treemap['aakash'] = User('aakash', 'Aakash R', 'aakashr@example.com')
    # print(treemap['aakash'])

    for key, value in treemap:
        print('key: {}'.format(key))
        print('value: {}'.format(value))
        print()

    # print(list(treemap))
