'''
Author: Ronald Coello
Credits: Brigham Young University Idaho
ronaldcoello85@gmail.com
Implementation of a Tree
'''

class BST:

    class Node:

        def __init__(self, data):

            self.data = data
            self.left = None
            self.right = None
    
    def __init__(self):

        self.root = None
    
    def insert(self, data):

        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, node):
        
        # The data is less than current node, look for a place on the left
        if data <= node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        
        # The data is greater than the current node, look for a place on the right
        elif data >= node.data:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)

    def __contains__(self, data):

        return self._contains(data, self.root)  # Start at the root


    def _contains(self, data, node):

        if data == node.data:
            return True
        if node.left is not None:
            if node.data > data:
                return self._contains(data, node.left)
        if node.right is not None:    
            if node.data < data:
                return self._contains(data, node.right)

    def __iter__(self):

        yield from self._traverse_forward(self.root)  # Start at the root
            
    def _traverse_forward(self, node):

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
  
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):

        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)   # Replace this when you implement your solution
    
    def get_height(self):

        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    def _get_height(self, node):

        h_l = 1
        h_r = 1
        if node.left is None and node.right is None:
            return 1
        if node.left is not None:
            h_l = 1 + self._get_height(node.left)
        if node.right is not None:
            h_r = 1 + self._get_height(node.right)
        
        return max(h_l, h_r)

print('===============Test Cases===============')
tree = BST()
tree.insert(9)
tree.insert(5)
tree.insert(1)
tree.insert(8)
tree.insert(10)

for i in tree:
    print(i)

print(2 in tree) # False
print(10 in tree) # True
print(3 in tree) # False
print(9 in tree) # True