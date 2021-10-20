"""Linked list class, realizing two-bounded circle list"""
from Composition import Composition
from LinkedListItem import LinkedListItem


class LinkedList:
    def __init__(self):
        self.first_item = None
        self.last_item = None
        self.length = 0
        self.iteration = None
        self.count_of_iteration = 0

    def __create_list(self, item):
        """Initialize list"""
        new_item = LinkedListItem(None, item, None)
        self.first_item = new_item
        self.last_item = new_item
        self.length += 1

    def append_left(self, item):
        """Append item in the begin of the list"""
        if self.first_item is None:
            self.__create_list(item)
            return
        else:
            new_item = LinkedListItem(self.first_item, item, self.last_item)
            self.first_item.previous_link = new_item
            self.first_item = new_item
            self.length += 1
            return

    def append_right(self, item):
        """Append item in the end of the list"""
        if self.first_item is None:
            self.__create_list(item)
            return
        else:
            new_item = LinkedListItem(self.first_item, item, self.last_item)
            self.last_item.next_link = new_item
            self.last_item = new_item
            self.length += 1
            return

    def remove(self, item):
        """Remove item from the list"""
        iteration_item = self.first_item
        for i in range(self.length):
            if iteration_item == item:
                if iteration_item == self.first_item:
                    new_first_item = iteration_item.next_link
                    new_first_item.previous_link = self.last_item
                    self.last_item.next_link = new_first_item
                    self.first_item = new_first_item
                    self.length -= 1
                    return
                if iteration_item == self.last_item:
                    new_last_item = iteration_item.previous_link
                    new_last_item.next_link = self.first_item
                    self.first_item.previous_link = new_last_item
                    self.last_item = new_last_item
                    self.length -= 1
                    return
                else:
                    previous_item = iteration_item.get_previous_link
                    next_item = iteration_item.next_link
                    previous_item.next_link = next_item
                    next_item.previous_link = previous_item
                    self.length -= 1
                    return
            else:
                iteration_item = iteration_item.next_link
        raise ValueError("Данного элемента в списке нет")

    def insert(self, previous_item, new_item):
        """Insert item in the position after previous_item"""
        iteration_item = self.first_item
        if isinstance(new_item, Composition):
            new_item = LinkedListItem(None, new_item, None)
        for i in range(self.length):
            if iteration_item == previous_item:
                if iteration_item == self.last_item:
                    self.last_item.next_link = new_item
                    new_item.previous_link = self.last_item
                    new_item.next_link = self.first_item
                    self.last_item = new_item
                    self.first_item.previous_link = self.last_item
                    self.length += 1
                    return
                else:
                    new_item = previous_item.next_link
                    previous_item.next_link = new_item
                    new_item.previous_link = new_item
                    new_item.next_link = new_item
                    new_item.previous_link = previous_item
                    self.length += 1
                    return
            else:
                iteration_item = iteration_item.next_link
        raise ValueError("Элемент, после которого вы хотите вставить новый, не существует")

    def replace(self, previous_item, replaced_item):
        """Replace item in the position after previous_item"""
        iteration_item = self.first_item
        for i in range(self.length):
            if iteration_item == replaced_item:
                if previous_item == self.last_item and replaced_item == self.first_item:
                    pass
                if previous_item == self.last_item:
                    pass
                else:
                    pass
            else:
                iteration_item = iteration_item.next_link
        raise ValueError("Элемент, после которого вы хотите переместить другой, не существует")

    def last(self):
        """Return last item of the list"""
        return self.last_item

    def take_item(self, data):
        """Take item from the list according to the data"""
        iteration_item = self.first_item
        for i in range(self.length):
            if iteration_item.data == data:
                return iteration_item
            iteration_item = iteration_item.next_link
        raise ValueError("Такого элемента не существует")

    def __len__(self):
        return self.length

    def __iter__(self):
        self.iteration = self.first_item
        self.count_of_iteration = 1
        return self

    def __next__(self):
        iteration_item = self.iteration
        self.iteration = self.iteration.next_link
        if self.count_of_iteration <= self.length:
            self.count_of_iteration += 1
        else:
            raise StopIteration("Stop")
        return iteration_item

    def __getitem__(self, index):
        if -self.length <= index <= -1:
            index = self.length + index
        iteration_item = self.first_item
        iteration_index = 0
        for i in range(self.length):
            if iteration_index == index:
                return iteration_item
            else:
                iteration_index += 1
            iteration_item = iteration_item.next_link
        raise IndexError("Неверный индекс")

    def __contains__(self, item):
        iteration_item = self.first_item
        for i in range(self.length):
            if iteration_item == item:
                return True
            iteration_item = iteration_item.next_link
        return False

    def __reversed__(self):
        pass
