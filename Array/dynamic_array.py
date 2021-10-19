"""Класс массива"""

from my_array import array


class Array:
    """Сам массив"""
    def __init__(self, typecode, initializer):
        self.typecode = typecode
        self.my_array = initializer
        self.lenght = len(initializer)

    def append(self, item):
        """Добавление элемента"""
        if self.typecode == 'd':
            self.my_array.append(float(item))
        elif self.typecode == 'i':
            self.my_array.append(int(item))

    def print(self):
        print(str(self[:]))

    def insert(self, index, item):
        """Вставка"""
        if self.typecode == 'd':
            self.my_array.insert(index, float(item))
        elif self.typecode == 'i':
            self.my_array.insert(index, int(item))

    def remove(self, item):
        """Удаление"""
        self.my_array.remove(item)

    def pop(self, index):
        """Удаление с возвратом"""
        return self.my_array.pop(index)

    def len(self):
        return self.lenght

    def reverse(self):
        return self.__reversed__()

    """ "Магические" методы"""
    def __getitem__(self, index):
        return self.my_array[index]

    def __setitem__(self, index, value):
        self.my_array[index] = value

    def __reversed__(self):
        return self.__class__(self.typecode, list(reversed(self.my_array)))

    def __len__(self):
        return len(self.my_array)

    def __sizeof__(self):
        return self.my_array.__sizeof__()

    def __eq__(self, o: object):
        if isinstance(o, array):
            return o.typecode == self.typecode and list(o) == self.my_array
        return False
