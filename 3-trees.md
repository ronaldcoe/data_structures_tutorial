# Trees

A tree is a data structur similar to a linked list in that nodes are connected by pointers; however, unlike linked lists, trees are nonlinear, meaning that a tree can connect to multiple nodes. 
</br>
In this tutorial, we will talk about three different types of trees: binary trees, binary search trees, and balanced binary search trees.
<p align="center">
<img  width="500" src="resources/tree.jpg">
</p>

## Binary Trees
A binary tree is a tree that points to no more than two other nodes. The top node is refered as the root. A node that has connceted other nodes is called a parent node. Each node connected to a parent node is refered as the left child and the right child. Nodes that connect to no other nodes are called leaf nodes.
<p align="center">
<img  width="500" src="resources/binary tree.jpg">
</p>

## Binary search tree
A binary search tree is a tree that follows some rules to store data in the tree:
* The left child is always less than the parent node.
* The right child is always more than the parent node
<br>

By following these rules, we always know where to put additional items. One of the advantages of a binary search tree is that we can locate an element without the need of visiting every item in the tree.
<br>
