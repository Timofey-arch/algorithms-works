"""Linked list item class, realizing element of two-bounded circle list"""


class LinkedListItem:

    def __init__(self, next_link, data, previous_link):
        self.__next_link = next_link
        self.data = data
        self.__previous_link = previous_link

    @property
    def next_link(self):
        return self.__next_link

    @property
    def previous_link(self):
        return self.__previous_link

    @next_link.setter
    def next_link(self, link):
        self.__next_link = link

    @previous_link.setter
    def previous_link(self, link):
        self.__previous_link = link
