"""Тесты модуля linked_list"""

import unittest

from LinkedList import LinkedListItem, LinkedList

TEST_LEN = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]

TEST_LAST = TEST_LEN

TEST_REMOVE = [
    ([1], 1),
    ([1, 1, 1], 1),
    ([2, 1, 1, 3], 1),
    ([2, 3, 4], 2),
    ([2, 3, 4], 4),
]

TEST_REMOVE_FAILED = [
    ([], 1),
    ([1], 2),
    ([1, 1, 1, 3, 4], 2),
]

TEST_CONTAINS = [
    ([], 1, False),
    ([1], 1, True),
    ([1], 2, False),
    ([1, 1, 1], 1, True),
    ([2, 3], 5, False),
    ([2, 3], 3, True),
]

TEST_GETITEM = [
    ([2], 0),
    ([4], -1),
    ([5, 1], 1),
    ([5, 1], -2),
    ([2, 0, 1, 4, 2], 2),
]

TEST_GETITEM_FAILED = [
    ([], 0),
    ([1], 1),
    ([1], -2),
    ([1, 2, 3], 3),
    ([1, 2, 4], -4),
]

TEST_INSERT = [
    ([1], 0, 42),
    ([1, 2, 3], 1, 42),
    ([1, 2, 3], 0, 42),
]


class TestLinkedListItem(unittest.TestCase):
    """Тест-кейс класса LinkedListItem"""

    def test_next_item(self):
        """Тест соединения узлов через next_item"""
        node_a = LinkedListItem(None, 42, None)
        node_b = LinkedListItem(None, 196, None)
        node_a.next_link = node_b
        self.assertTrue(node_a.next_link is node_b)
        self.assertTrue(node_a.previous_link is None)
        self.assertTrue(node_b.next_link is None)

    def test_previous_item(self):
        """Тест соединения узлов через previous_item"""
        node_a = LinkedListItem(None, 42, None)
        node_b = LinkedListItem(None, 196, None)
        node_b.previous_link = node_a
        self.assertTrue(node_a.previous_link is None)
        self.assertTrue(node_b.next_link is None)
        self.assertTrue(node_b.previous_link is node_a)


class TestLinkedList(unittest.TestCase):
    """Тест-кейс класса LinkedList"""

    def test_len(self):
        """Тест метода len"""
        for expected_len in TEST_LEN:
            linked_list = LinkedList()
            for i in range(expected_len):
                linked_list.append_right(1)
            with self.subTest(expected_len=expected_len):
                self.assertEqual(len(linked_list), expected_len)

    def test_last(self):
        """Тест свойства last"""
        for expected_len in TEST_LAST:
            linked_list = LinkedList()
            for i in range(expected_len):
                linked_list.append_right(1)
            with self.subTest(expected_len=expected_len):
                self.assertEqual(linked_list.last(), linked_list.last_item)

    def test_append_left(self):
        """Тест метода append_left"""
        for expected_len in TEST_LEN:
            linked_list = LinkedList()
            last_first = 0
            first_first = 0
            for i in range(expected_len):
                first_first = linked_list.first_item
                linked_list.append_left(1)
                last_first = linked_list.first_item.next_link
            with self.subTest(expected_len=expected_len):
                self.assertEqual(first_first, last_first)

    def test_append_right(self):
        """Тест метода append_right"""
        for expected_len in TEST_LEN:
            linked_list = LinkedList()
            with self.subTest(expected_len=expected_len):
                appended_item = LinkedListItem(None, 42, None)
                linked_list.append_right(appended_item)
                self.assertEqual(linked_list.last(), appended_item)

    def test_remove(self):
        """Тест метода remove"""
        for elements, removed_element in TEST_REMOVE:
            linked_list = LinkedList()
            for i in range(len(elements)):
                linked_list.append_right(elements[i])
            with self.subTest(elements=elements, removed_element=removed_element):
                linked_list.remove(removed_element)
                self.assertEqual(len(linked_list), len(elements) - 1)

    def test_remove_failed(self):
        """Тест метода remove с исключением ValueError"""
        for node_list, remove_item in TEST_REMOVE_FAILED:
            linked_list = LinkedList()
            for i in range(len(node_list)):
                linked_list.append_right(node_list[i])
            with self.subTest(node_list=node_list, remove_item=remove_item):
                with self.assertRaises(ValueError):
                    linked_list.remove(remove_item)

    def test_insert(self):
        """Тест метода insert"""
        for node_list, index, data in TEST_INSERT:
            linked_list = LinkedList()
            for i in range(len(node_list)):
                linked_list.append_right(node_list[i])
            with self.subTest(node_list=node_list, index=index,
                              data=data):
                linked_list.insert(linked_list[index], data)
                self.assertEqual(len(linked_list), len(node_list) + 1)
                node_list.insert(index + 1, data)
                self.assertEqual([i.data for i in linked_list], node_list)

    def test_getitem(self):
        """Тест индексации"""
        for node_list, index in TEST_GETITEM:
            linked_list = LinkedList()
            for i in range(len(node_list)):
                linked_list.append_right(node_list[i])
            with self.subTest(node_list=node_list, index=index):
                item = linked_list[index]
                self.assertEqual(item, node_list[index])

    def test_getitem_failed(self):
        """Тест индексации с исключением IndexError"""
        for node_list, index in TEST_GETITEM_FAILED:
            linked_list = LinkedList()
            for i in range(len(node_list)):
                linked_list.append_right(node_list[i])
            with self.subTest(node_list=node_list, index=index):
                with self.assertRaises(IndexError):
                    _ = linked_list[index]

    def test_contains(self):
        for node_list, item, expected in TEST_CONTAINS:
            linked_list = LinkedList()
            for i in range(len(node_list)):
                linked_list.append_right(node_list[i])
            with self.subTest(node_list=node_list, item=item, expected=expected):
                self.assertTrue((item in linked_list) is expected)
