"""Linked list class, realizing two-bounded circle list"""
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
        if not isinstance(item, LinkedListItem):
            item = LinkedListItem(None, item, None)
        self.first_item = item
        self.last_item = item
        self.first_item.previous_link = self.last_item
        self.last_item.next_link = self.first_item
        self.length += 1

    def append_left(self, item):
        """Append item in the begin of the list"""
        if self.first_item is None:
            self.__create_list(item)
            return
        else:
            if not isinstance(item, LinkedListItem):
                item = LinkedListItem(None, item, None)
            self.first_item.previous_link = item
            item.next_link = self.first_item
            self.first_item = item
            self.first_item.previous_link = self.last_item
            self.last_item.next_link = self.first_item
            self.length += 1
            return

    def append_right(self, item):
        """Append item in the end of the list"""
        if self.first_item is None:
            self.__create_list(item)
            return
        else:
            if not isinstance(item, LinkedListItem):
                item = LinkedListItem(None, item, None)
            self.last_item.next_link = item
            item.previous_link = self.last_item
            self.first_item.previous_link = item
            self.last_item = item
            self.last_item.next_link = self.first_item
            self.length += 1
            return

    def remove(self, item):
        """Remove item from the list"""
        iteration_item = self.first_item
        if not isinstance(item, LinkedListItem):
            item = self.take_item(item)
        if self.first_item == self.last_item:
            self.first_item = None
            self.last_item = None
            self.length = 0
            return
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
                    previous_item = iteration_item.previous_link
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
        if not isinstance(new_item, LinkedListItem):
            new_item = LinkedListItem(None, new_item, None)
        if not isinstance(previous_item, LinkedListItem):
            previous_item = self.take_item(previous_item)
        for i in range(self.length):
            if iteration_item == previous_item:
                if iteration_item == self.last_item:
                    self.last_item.next_link = new_item
                    new_item.previous_link = self.last_item
                    self.last_item = new_item
                    self.last_item.next_link = self.first_item
                    self.first_item.previous_link = self.last_item
                    self.length += 1
                    return
                else:
                    next_item = previous_item.next_link
                    new_item.next_link = next_item
                    new_item.previous_link = previous_item
                    previous_item.next_link = new_item
                    next_item.previous_link = new_item
                    self.length += 1
                    return
            else:
                iteration_item = iteration_item.next_link
        raise ValueError("Элемент, после которого вы хотите вставить новый, не существует")

    def replace(self, previous_item, item):
        iteration_item = self.first_item
        replaced_item = item
        for i in range(self.length):
            if iteration_item == item:
                self.remove(item)
                self.insert(previous_item, replaced_item)
                return
            else:
                iteration_item = iteration_item.next_link
        raise ValueError("Элемент после которого вы хотите переместить, не существует")

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
                return iteration_item.data
            else:
                iteration_index += 1
            iteration_item = iteration_item.next_link
        raise IndexError("Неверный индекс")

    def __contains__(self, item):
        iteration_item = self.first_item
        for i in range(self.length):
            if iteration_item.data == item:
                return True
            iteration_item = iteration_item.next_link
        return False
