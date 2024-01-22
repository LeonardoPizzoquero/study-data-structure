import unittest
from LL import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList(1)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.append(4)
        self.ll.append(5)

    def test_append(self):
        self.assertEqual(self.ll.length, 5)
        self.assertEqual(self.ll.tail.value, 5)

    def test_pop(self):
        popped = self.ll.pop()
        self.assertEqual(popped.value, 5)
        self.assertEqual(self.ll.length, 4)
        self.assertEqual(self.ll.tail.value, 4)

    def test_prepend(self):
        self.ll.prepend(0)
        self.assertEqual(self.ll.length, 6)
        self.assertEqual(self.ll.head.value, 0)

    def test_pop_first(self):
        popped = self.ll.pop_first()
        self.assertEqual(popped.value, 1)
        self.assertEqual(self.ll.length, 4)
        self.assertEqual(self.ll.head.value, 2)

    def test_get_by_index(self):
        node = self.ll.get_by_index(2)
        self.assertEqual(node.value, 3)

    def test_get_by_value(self):
        node = self.ll.get_by_value(4)
        self.assertEqual(node.value, 4)

    def test_set(self):
        self.ll.set(2, 10)
        node = self.ll.get_by_index(2)
        self.assertEqual(node.value, 10)

    def test_insert(self):
        self.ll.insert(2, 10)
        self.assertEqual(self.ll.length, 6)
        node = self.ll.get_by_index(2)
        self.assertEqual(node.value, 10)

    def test_remove(self):
        removed = self.ll.remove(2)
        self.assertEqual(removed.value, 3)
        self.assertEqual(self.ll.length, 4)
        node = self.ll.get_by_index(2)
        self.assertEqual(node.value, 4)

    def test_reverse(self):
        self.ll.reverse()
        self.assertEqual(self.ll.head.value, 5)
        self.assertEqual(self.ll.tail.value, 1)

if __name__ == '__main__':
    unittest.main()