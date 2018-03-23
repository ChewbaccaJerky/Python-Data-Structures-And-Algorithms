import bst_node as BSTNode

class BinarySearchTree:

     def __init(self):
         self.root = None

    def insert(value):
        node = BSTNode.new(value)
        if self.root == None:
            self.root = node
            return
        self.insert_into_position(node)

    def insert_into_position(node, tree_node = self.root):
        # 1. Compare
        comp = -1 if node.value <= tree_node.value else 1

        if comp == -1:
            # 2a. Sets left child if it is nil
            if tree_node.left == None:
                node.parent = tree_node
                tree_node.left = node
            # 2b. Enter left subtree
            else:
                insert_into_position(node, tree_node.left)
        elif comp == 1:
            # 3a. Sets right child if it is nil
            if tree_node.right == None:
                node.parent = tree_node
                tree_node.right = node
            # 3b. Enter right subtree
            else:
                insert_into_position(node, tree_node.right)

    def find(value, tree_node = self.root):
        return None if tree_node == None
        # 1. Return if value found
        if value == tree_node.value:
            return tree_node
        # 2. If value is less the current node
        # enter left subtree
        elif value < tree_node.value:
            find(value, tree_node.left)
        # 3. If value is greater than the current node
        # enter right subtree
        else:
            find(value, tree_node.right)

    def delete(value):
        # 1. find node
        node = find(value)

        # 2. calculate number of children
        num_kids = 0
        num_kids += 1 if node.left
        num_kids += 1 if node.right

        if num_kids == 0:
            remove_childless_node(node)
        elif num_kids == 1:
            remove_one_child_node(node)
        else
            remove_two_child_node(node)

        # 3. Detach node
        node.left = None
        node.right = None

    def remove_childless_node(node):
        # case 1: node is root
        if node == self.root:
            self.root = None
        else:
            parent = node.parent
            parent.right = None if parent.right == node else parent.left = None

    def remove_one_child_node(node):
        child = node.left if node.left else node.right
        
        # case 1 node is root
        if node == self.root:
            self.root = child
        else:
            parent = node.parent
            child.parent = child.parent.parent
            parent.right = child if parent.right == node else parent.left = child

    def maximum(tree_node = self.root):
        return tree_node if tree_node.right == None
        maximum(tree_node.right)

    def remove_two_child_node(node):
        # step 1 get max on left subtree
        max = self.maximum(node.left)

        if node != self.root:
            delete(max.value)
            node.parent.right = max if node.parent.right == node else node.parent.left = max
        
        max.left = node.left
        max.right = max.right
        