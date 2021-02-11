import unittest
from linked_list import MyLinkedList, Node


class MyTestCase(unittest.TestCase):
    def test_add_reverse(self):
        print('Test: Empty list(s)')
        self.assertEqual(MyLinkedList().add_reverse(None, None), None)
        self.assertEqual(MyLinkedList().add_reverse(Node(5), None), None)
        self.assertEqual(MyLinkedList().add_reverse(None, Node(10)), None)

        print('Test: add values of different length')
        # input 1 : 6->5->None
        # input 2 : 9->8->7
        # result : 5->4->8
        first_list = MyLinkedList(Node(6))
        first_list.append(5)
        second_list = MyLinkedList(Node(9))
        second_list.append(8)
        second_list.append(7)
        result = MyLinkedList().add_reverse(first_list, second_list)
        self.assertEqual(result.get_all_data(), [5, 4, 8])

        print('Test: add values of same length')
        # input 1 : 6->5->4
        # input 2 : 9->8->7
        # result : 5->4->2->1
        first_list = MyLinkedList(Node(6))
        first_list.append(5)
        first_list.append(4)

        second_list = MyLinkedList(Node(9))
        second_list.append(8)
        second_list.append(7)

        result = MyLinkedList().add_reverse(first_list, second_list)
        self.assertEqual(result.get_all_data(), [5, 4, 2, 1])

        print('Success: test_add_reverse')

    def test_add_node(self):
        print('Test: Empty list, null node to delete')
        linked_list = MyLinkedList(None)
        linked_list.delete_node(None)
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: One node')
        head = Node(2)
        linked_list = MyLinkedList(head)
        linked_list.delete_node(head)
        self.assertEqual(linked_list.get_all_data(), [None])

        print('Test: Multiple nodes')
        linked_list = MyLinkedList(None)
        node0 = linked_list.insert_to_front(2)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node1)
        self.assertEqual([1, 4, 2], linked_list.get_all_data())

        print('Test: Multiple nodes, delete last element')
        linked_list = MyLinkedList(None)
        node0 = linked_list.insert_to_front(2)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node0)
        self.assertEqual([1, 4, 3, None], linked_list.get_all_data())

        print('Success: test_delete_node')

    def test_find_loop_start(self):
        print("Test: Empty list")
        linked_list = MyLinkedList()
        self.assertEqual(None, linked_list.find_loop_start())

        print("Test: Not a circular linked list: One element")
        head = Node(1)
        linked_list = MyLinkedList(head)
        self.assertEqual(None, linked_list.find_loop_start())

        print("Test: Not a circular linked list: Two elements")
        linked_list.append(2)
        self.assertEqual(None, linked_list.find_loop_start())

        print("Test:: Not a circular linked list: Three or more elements")
        linked_list.append(3)
        self.assertEqual(None, linked_list.find_loop_start())

        print('Test: General case: Circular linked list')
        node10 = Node(10)
        node9 = Node(9, node10)
        node8 = Node(8, node9)
        node7 = Node(7, node8)
        node6 = Node(6, node7)
        node5 = Node(5, node6)
        node4 = Node(4, node5)
        node3 = Node(3, node4)
        node2 = Node(2, node3)
        node1 = Node(1, node2)
        node0 = Node(0, node1)
        node10.next = node3
        linked_list = MyLinkedList(node0)
        self.assertEqual(node3, linked_list.find_loop_start())

        print("Success: test_find_loop_start")

    def test_kth_to_last_elem(self):
        print('Test: empty list')
        linked_list = MyLinkedList()
        self.assertEqual(linked_list.kth_to_last_elem(0), None)

        print('Test: k >= len(list)')
        self.assertEqual(linked_list.kth_to_last_elem(100), None)

        print('Test: one element, k = 0')
        # linked_list.append(1)
        linked_list = MyLinkedList(Node(1))
        self.assertEqual(linked_list.kth_to_last_elem(0), 1)

        print('Test: general case')
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(5)
        linked_list.insert_to_front(7)
        self.assertEqual(linked_list.kth_to_last_elem(2), 3)

        print('Success: test_kth_to_last_elem')

    def test_insert_to_front(self):
        print('Test: insert_to_front on an empty list')
        linked_list = MyLinkedList(None)
        linked_list.insert_to_front(10)
        self.assertEqual([10], linked_list.get_all_data())

    def test_append(self):
        print('Test: append on an empty list')
        linked_list = MyLinkedList(None)
        linked_list.append(10)
        self.assertEqual([10], linked_list.get_all_data())

    def test_find(self):
        print('Test: find on an empty list')
        linked_list = MyLinkedList(None)
        node = linked_list.find('a')
        self.assertEqual(None, node)

    def test_delete(self):
        print('Test: delete on an empty list')
        linked_list = MyLinkedList(None)
        linked_list.delete('a')
        self.assertEqual([], linked_list.get_all_data())

    def test_len(self):
        print('Test: len on an empty list')
        linked_list = MyLinkedList(None)
        self.assertEqual(0, len(linked_list))

    def test_palindrome(self):
        print('Test: empty list')
        linked_list = MyLinkedList(None)
        self.assertEqual(False, linked_list.is_palindrome())

        print('Test: single element list')
        head = Node(1)
        linked_list = MyLinkedList(head)
        self.assertEqual(False, linked_list.is_palindrome())

        print('Test: two element list, not a palindrome')
        linked_list.append(2)
        self.assertEqual(False, linked_list.is_palindrome())

        print('Test: General case: Palindrome with even length')
        head = Node('a')
        linked_list = MyLinkedList(head)
        linked_list.append('b')
        linked_list.append('b')
        linked_list.append('a')
        self.assertEqual(True, linked_list.is_palindrome())

        print('Test: General case: Palindrome with odd length')
        head = Node(1)
        linked_list = MyLinkedList(head)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)

        self.assertEqual(linked_list.is_palindrome(), True)
        print('Success: test_palindrome')

    def test_partition(self):
        print('Test: Partition on an empty list')
        linked_list = MyLinkedList(None)
        linked_list.partition(10)
        self.assertEqual([], linked_list.get_all_data())

        print('Test: Partition on one element list, left list is empty')
        linked_list.append(1)
        linked_list.partition(10)
        self.assertEqual([1], linked_list.get_all_data())

        print('Test: right list is empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(10)
        self.assertEqual([5], linked_list.get_all_data())

        print('General case')
        linked_list = MyLinkedList(Node(12))

        linked_list.insert_to_front(10)

        linked_list.insert_to_front(14)

        linked_list.insert_to_front(1)

        linked_list.insert_to_front(10)

        linked_list.insert_to_front(8)

        linked_list.insert_to_front(13)

        linked_list.insert_to_front(3)

        linked_list.insert_to_front(4)
        partition_list = linked_list.partition(10)
        self.assertEqual([4, 3, 8, 1, 10, 10, 13, 14, 12], partition_list.get_all_data())

        print("Success: test_partition")

    def test_remove_dupes(self):
        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        linked_list.remove_dupes()
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: One element list')
        linked_list.insert_to_front(2)
        linked_list.remove_dupes()
        self.assertEqual(linked_list.get_all_data(), [2])

        print('Test: General case, duplicates')
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(2)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(1)
        linked_list.remove_dupes()
        self.assertEqual(linked_list.get_all_data(), [1, 3, 2])

        print('Test: General case, no duplicates')
        linked_list.remove_dupes()
        self.assertEqual(linked_list.get_all_data(), [1, 3, 2])

        print('Success: test_remove_dupes\n')


if __name__ == '__main__':
    unittest.main()
