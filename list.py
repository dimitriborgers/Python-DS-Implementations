import ctypes

class DynamicArray:

    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._data = self._make_array(self._capacity)

    def __len__(self):
        return self._size

    def __getitem__(self,index):
        if not 0 <= index < self._size:
            raise IndexError('Invalid Index')
        else:
            return self._data[index]

    def append(self,element):
        if self._size == self._capacity:
            self.resize()
        self._data[self._size] = element
        self._size += 1

    def _resize(self):
        new = self._make_array(self.capacity*2)
        for i in range(self._size):
            new[i] = self._data[i]
        self._data = new
        self._capacity *= 2

    def _make_array(self,c):
        return (c*ctypes.py_object)()
        
#------------------------------------------------------
