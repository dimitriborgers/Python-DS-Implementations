class SinglyLinkedStack:

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
    
#------------------------------------------------------

class SinglyLinkedQueue:

    class _Node:
        __slots__ = '_element','_next'

        def __init__(self, _element, _next):
            self._element = _element
            self._next = _next

    def __init__(self):
        self._head = None
        self._tail = None
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

    def first(self):
        if self.is_empty():
            raise Exception('Queue is Empty')
        else:
            return self._head._element

    def enqueue(self,e):
        if self.is_empty():
            self._tail = self._head = self._Node(e,None)
        else:
            self._tail._next = self._tail = self._Node(e,None)
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return Exception('Queue is Empty')
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return result

#------------------------------------------------------
    
class CircularyLinkedQueue:

    class _Node:
        __slots__ = '_element','_next'

        def __init__(self, _element, _next):
            self._element = _element
            self._next = _next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        if self.is_empty():
            return "[]"
        outcome = []
        current = self._head
        outcome.append(current._element)
        while current._next != self._head:
            outcome.append(current._next._element)
            current = current._next
        return "{}".format(outcome)

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception('Queue is Empty')
        else:
            return self._head._element

    def enqueue(self,e):
        newest = self._Node(e,None)
        if self.is_empty():
            self._tail = self._head = newest
            newest._next = newest
        else:
            self._tail._next = self._tail = newest
            self._tail._next = self._head
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return Exception('Queue is Empty')
        result = self._head._element
        if self._size == 1:
            self._tail = self._head = None
        else:
            self._tail._next = self._head = self._head._next
        self._size -= 1
        return result

    def rotate(self):
        oldhead = self._head
        self._head = self._head._next
        self._tail = oldhead

#------------------------------------------------------
        
class _DoublyLinkedList:

    class _Node:
        __slots__ = '_element','_next','_previous'

        def __init__(self, _element, _previous, _next):
            self._element = _element
            self._previous = _previous
            self._next = _next

    def __init__(self):
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._previous = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        outcome = []
        current = self._header._next
        while current != self._trailer:
            outcome.append(current._element)
            current = current._next
        return "{}".format(outcome)

    def is_empty(self):
        return self._size == 0

    def _insert_between(self,e,left,right):
        newest = self._Node(e,left,right)
        left._next = newest
        right._previous = newest
        self._size += 1

    def _delete_node(self,node):
        left = node._previous
        right = node._next
        left._next = right
        right._previous = left
        self._size -= 1
        element = node._element
        node._previous = node._next = node._element = None
        return element
    
#------------------------------------------------------

class PositionalList(_DoublyLinkedList):

    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not(self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self,node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self,node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._next)

    def before(self,p):
        node = self._validate(p)
        return self._make_position(node._previous)

    def after(self,p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def __repr__(self):
        outcome = []
        current = self._header._next
        while current != self._trailer:
            outcome.append(current._element)
            current = current._next
        return '{}'.format(outcome)

    def _insert_between(self,e,predecessor,successor):
        node = super()._insert_between(e,predecessor,successor)
        return self._make_position(node)

    def add_first(self,e):
        return self._insert_between(e,self._header,self._header._next)

    def add_last(self,e):
        return self._insert_between(e,self._trailer._previous,self._trailer)

    def add_before(self,p,e):
        original = self._validate(p)
        return self._insert_between(e, original._previous, original)

    def add_after(self,p,e):
        original = self._validate(p)
        return self._insert_between(e,original, original._next)

    def delete(self,p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self,p,e):
        original - self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
  
    
