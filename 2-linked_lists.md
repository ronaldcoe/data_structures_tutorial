# Linked Lists
Linked lists are characterized for no continuos memory. Unlike dynamic arrays that each element is right next to each other, a collection of data in a linked list can be stored randomly in memory. There is no garantee that one element is next to another. But, how could we keep our elements together?<br>
In order to keep our collection together, every element (called a **node**) will have a **value** and a reference that pointing to the next **node**
## Head and tail
If we want traverse through our linked list, we will need to know where to begin and where to end. The first node in the linked list is refered as the **head** or the begining of the collection, and the last node is refered as the **tail**. 
Most linked lists use a bi-directional linking between nodes. This meas that each node will mantain a pointer to both the next element and the previous.