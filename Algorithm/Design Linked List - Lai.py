"""
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list.
 A node in a singly linked list should have two attributes: val and next. val is the value of the current node,
 and next is a pointer/reference to the next node. If you want to use the doubly linked list,
 you will need one more attribute prev to indicate the previous node in the linked list.
 Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) :             Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) :         Add a node of value val before the first element of the linked list.
                         After the insertion, the new node will be the first node of the linked list.
addAtTail(val) :         Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list.
                         If index equals to the length of linked list, the node will be appended to the end of linked
                         list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) :   Delete the index-th node in the linked list, if the index is valid.
Example:

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
Note:

All values will be in the range of [1, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in LinkedList library.
"""
""" 
Method 2: use doubly linked list 
Time: O(n）
Space: O(1)

                                        TO DO ... 
"""




""" 
Method 1: use singly linked list 
Time: O(n）
Space: O(1)
"""


class _ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # the internal singly linked list
        self._head = None
        self._size = 0
        self._tail = None

    def _get(self, index):
        # assume index is within [0, self._size)
        node = self._head
        for i in range(index):
            node = node.next
        return node

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self._size:
            return -1
        return self._get(index).val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion,
        the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        # if head is None
        node = _ListNode(val)
        if self._size == 0:
            self._head = self._tail = node
        else:
            new_head = node
            new_head.next = self._head
            self._head = new_head

        self._size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        node = _ListNode(val)
        if self._size == 0:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node

        self._size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        node = _ListNode(val)
        if index < 0 or index > self._size:
            return

        if index == 0:
            self.addAtHead(val)
        elif index == self._size:
            self.addAtTail(val)
        else:
            prev_node = self._get(index - 1)
            node.next = prev_node.next
            prev_node.next = node
            self._size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self._size:
            return

        if index == 0:
            new_head = self._head.next
            # self._head.next = None
            self._head = new_head
            # if original head is length 1 and removed then tail is None
            if self._head is None:
                self._tail = None

        elif index == self._size - 1:
            self._tail = self._get(index - 1)
        else:
            prev_node = self._get(index - 1)
            # remove_node = prev_node.next
            prev_node.next = prev_node.next.next

        self._size -= 1

    def __str__(self):
        list = []
        node = self._head
        while node is not None:
            list.append(str(node.val))
            node = node.next
        return '->'.join(list)

# # Your Solution object will be instantiated and called as such:
# obj = Solution()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)