# cython: language_level = 3
# distutils: language = c
from cpython.mem cimport PyMem_Malloc, PyMem_Realloc, PyMem_Free
from cpython.float cimport PyFloat_FromDouble, PyFloat_AsDouble
from cpython.int cimport PyInt_AsLong

cdef struct arraydescr:
    char * typecode
    int itemsize
    object (*getitem)(array, int)
    int (*setitem)(array, int, py_object)

cdef object double_getitem(array a, int index):
    return (<double *> a.data)[index]

cdef int double_setitem(array a, int index, object obj):
    if not isinstance(obj, int) and not isinstance(obj, float):
        return -1

    cdef double value = PyFloat_AsDouble(obj)
    if index >= 0:
        (<double *> a.data)[index] = value
    return 0

cdef object int_getitem(array a, int index):
    return (<int *> a.data)[index]

cdef int int_setitem(array a, int index, object obj):
    if not isinstance(obj, int) and not isinstance(obj, float):
        return -1

    cdef int value = PyInt_AsLong(obj)
    if index >= 0:
        (<int *> a.data)[index] = value
    return 0

cdef arraydescr[2] descriptors = [
    arraydescr("d", sizeof(double), double_getitem, double_setitem),
    arraydescr("i", sizeof(int), int_getitem, int_setitem)
]

cdef enum TypeCode:
    INT = 1
    DOUBLE = 0

cdef int char_typecode_to_int(str typecode):
    if typecode == "d":
        return TypeCode.DOUBLE
    if typecode == "i":
        return TypeCode.INT
    return -1

def degree_of_two(number):
    if number == 0:
        return False
    if number == 1:
        return True
    if number & 1:
        return False
    return degree_of_two(number >> 1)

cdef class array:
    cdef public size_t length
    cdef char * data
    cdef arraydescr * descr
    cdef int capacity

    def __cinit__(self, str typecode, object obj):
        """Initializiting function"""
        self.length = len(obj)

        cdef int mtypecode = char_typecode_to_int(typecode)
        self.descr = &descriptors[mtypecode]
        self.capacity = self.length
        while not degree_of_two(self.capacity):
            self.capacity += 1
        self.data = <char *> PyMem_Malloc((self.capacity * 2) * self.descr.itemsize)

        for i in range(self.length):
            self.__setitem__(i, obj[i])
        if not self.data:
            raise MemoryError

    def __dealloc__(self):
        """Free function"""
        PyMem_Free(self.data)

    def initialize(self):
        """Initializiting function"""
        cdef int i
        for i in range(self.length):
            self.__setitem__(i, PyFloat_FromDouble(<double> i))

    def len(self):
        """Len calculating function"""
        return self.length

    def append(self, item):
        """Append function"""
        new_lenght = self.length + 1
        if self.capacity == new_lenght:
            self.capacity *= 2
            self.data = <char *> PyMem_Realloc(self.data, self.capacity * self.descr.itemsize)
        self.length += 1
        self.__setitem__(self.length - 1, item)

    def remove(self, item):
        """Remove function"""
        cdef int index
        for i in range(self.length):
            if self[i] == item:
                index = i
                break
        for i in range(index, self.length - 1):
            self[i] = self[i + 1]
        self.length -= 1
        if self.length * 2 < self.capacity:
            self.data = <char *> PyMem_Realloc(self.data, self.length * self.descr.itemsize)

    def insert(self, index, item):
        """Insert function"""
        if 0 <= index < self.length:
            self.data = <char *> PyMem_Realloc(self.data, (self.length + 1) * self.descr.itemsize)
            self.length, prev_element, next_element, self[index] = self.length + 1, self[index], 0, item
            for i in range(index + 1, self.length):
                next_element = self[i]
                self[i] = prev_element
                prev_element = next_element
        elif index >= self.length:
            self.append(item)
        else:
            self.data = <char *> PyMem_Realloc(self.data, (self.length + 1) * self.descr.itemsize)
            self.length, prev_element, next_element, self[index] = self.length + 1, self[index], 0, item
            for i in range(index, 0):
                next_element = self[i]
                self[i] = prev_element
                prev_element = next_element

    def pop(self, index):
        """Pop function"""
        if index < 0:
            if abs(index) > self.length:
                raise IndexError
            else:
                index = self.length + index
        else:
            if index >= self.length:
                raise IndexError
        deleted_element = self[index]
        for i in range(index, self.length - 1):
            self[i] = self[i + 1]
        self.length -= 1
        self.data = <char *> PyMem_Realloc(self.data, self.length * self.descr.itemsize)
        return deleted_element

    def reversed(self):
        """Reverse function"""
        swap, reverse_index  = 0, -1
        for i in range(self.length // 2):
            swap = self[i]
            self[i] = self[reverse_index]
            self[reverse_index] = swap
            reverse_index -= 1

    def __getitem__(self, int index):
        if 0 <= index < self.length:
            return self.descr.getitem(self, index)
        elif (self.length * (-1)) <= index <= -1:
            index = self.length + index
            return self.descr.getitem(self, index)
        else:
            raise IndexError

    def __setitem__(self, int index, object value):
        if 0 <= index < self.length:
            self.descr.setitem(self, index, value)
        elif (self.length * -1) <= index <= -1:
            index = self.length + index
            self.descr.setitem(self, index, value)
        else:
            raise IndexError

    def __len__(self):
        return self.length

    def __sizeof__(self):

        return

    def __eq__(self, array other):
        if isinstance(other, array):
            if self.length == other.length:
                for i in range(self.length):
                    if self[i] != other[i]:
                        return False
                return True
        return False
