from ll_node import LinkedListNode as Node

class LinkedList:
    
    def __init__(self):
        self.head = Node(None)

    def insert(self, value):
        new_node = Node(value)
        
        new_node.next = self.head.next
        self.head.next = new_node

    def delete(self, value):
        p = self.head

        while p.next.value != value:
            p = p.next

        q = p.next
        p.next = p.next.next
        q.next = None


