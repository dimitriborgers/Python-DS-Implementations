class LinkedStack:

    class _Node:
        __slots__ = '_element','_next'

        def __init__(self, _element, _next):
            self._element = _element
            self._next = _next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        outcome = []
        current = self._head
        while current:
            outcome.append(current._element)
            current = current._next
        return "{}".format(outcome)

    def is_empty(self):
        return self._size == 0

    def top(self):
        if self.is_empty():
            raise Exception('Stack is Empty')
        else:
            return self._head._element

    def add(self,e):
        self._head = self._Node(e,self._head)
        self._size += 1

    def pop(self):
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        return result
