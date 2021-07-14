class SinglyLinkedList:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
		
    def add_first(self, e):
        self._head = self._Node(e, self._head)
        if self.is_empty():
            self._tail = self._head
        self._size += 1

    def add_last(self, e):
        newnode = self._Node(e, None)
        if self.is_empty():
            self._head = newnode
        else:
            self._tail._next = newnode
        self._tail = newnode
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty('Linked list is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def remove_last(self):
        if self.is_empty():
            raise Empty('Linked list is empty')
        if self._size == 1:
            answer = self._head._element
            self._head = None
            self._tail = None
        else:
            answer = self._tail._element
            current_node = self._head
            next_node = current_node._next
            while next_node != self._tail:
                current_node = next_node
                next_node = next_node._next
            self._tail = current_node
        self._size -= 1
        return answer

    def reverse(self):
        current = self._head
        prev = None
        next = current._next

        while current:
            # takes the current node and sets that node to point to the previous node
            # in turn reversing the direction that the nodes are pointing
            current = self._Node(current._element, prev)

            # this moves the previous node up to the current node
            # while also moving the current node to the next node
            prev = current
            current = next
            if next:
                next = next._next
        # this sets the head as the last value in the linked list
        self._head = prev