# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def delete_nodes(head, target):
    """
    Time: O(n)
    Space: O(1)
    """
    # write your solution here
    """corner cases"""
    if head is None:
        return head

    # create new dummy head due to head might change
    new_head = ListNode(None)
    new_head.next = head
    cur = head
    # head = new_head
    prev = new_head

    while cur is not None:
        if cur.val == target:
            prev.next = cur.next
        else:
            prev = prev.next

        cur = cur.next

    return new_head.next


n1 = ListNode(10); n2 = ListNode(8); n3= ListNode(5); n4 = ListNode(1); n5 = ListNode(8)
n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n5;

print(delete_nodes(n1, 8))