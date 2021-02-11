class Node:
    def __init__(self, value, node=None):
        self.data = value
        self.next = node


class LinkedList(object):
    def __init__(self, node=None):
        self.head = node

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return node
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(value)


class MyLinkedList(LinkedList):
    def __len__(self) -> int:
        curr = self.head
        counter = 0
        while curr is not None:
            curr = curr.next
            counter += 1
        return counter

    def insert_to_front(self, data):
        if data is None:
            return None
        tmp = Node(data, self.head)
        self.head = tmp
        return tmp

    def find(self, data):
        if data is None:
            return None
        curr = self.head
        while curr is not None:
            if curr.data == data:
                return curr
            curr = curr.next
        return None

    def delete(self, data):
        if data is None:
            return None
        if self.head is None:
            return None
        cur = self.head.next
        prev = self.head
        while cur is not None:
            if cur.data == data:
                prev.next = cur.next
                return
            cur = cur.next
            prev = prev.next

    def print_list(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_all_data(self):
        data = []
        cur = self.head
        while cur is not None:
            data.append(cur.data)
            cur = cur.next
        return data

    def _add_reverse(self, first_node, second_node, carry):
        if first_node is None and second_node is None and not carry:
            return None
        # Recursive case
        value = carry
        value += first_node.data if first_node is not None else 0

        value += second_node.data if second_node is not None else 0

        carry = 1 if value >= 10 else 0

        value %= 10

        node = Node(value)

        node.next = self._add_reverse(
            first_node.next if first_node is not None else None,
            second_node.next if second_node is not None else None,
            carry)

        return node

    def add_reverse(self, first_list, second_list):
        if first_list is None or second_list is None:
            return None

        head = self._add_reverse(first_list.head, second_list.head, 0)

        return MyLinkedList(head)

    @classmethod
    def delete_node(cls, node: Node):
        if node is None:
            return
        if node.next is None:
            node.data = None
        else:
            node.data = node.next.data
            node.next = node.next.next

    def find_loop_start(self):
        """
        empty list -> None
        Not circle list -> None
        """
        if self.head is None or self.head.next is None:
            return None
        slow = self.head
        fast = self.head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is None:
                return None
            if slow == fast:
                break
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
        return slow

    def kth_to_last_elem(self, k):
        if self.head is None:
            return None
        fast = self.head
        slow = self.head

        for _ in range(k):
            fast = fast.next
            if fast is None:
                return None

        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        return slow.data

    def is_palindrome(self):
        if self.head is None or self.head.next is None:
            return False
        curr = self.head
        reverse_list = MyLinkedList(None)
        length = 0
        while curr:
            reverse_list.insert_to_front(curr.data)
            curr = curr.next
            length += 1

        iterations = length // 2
        curr = self.head
        curr_reversed = reverse_list.head
        for _ in range(iterations):
            if curr.data != curr_reversed.data:
                return False
            curr = curr.next
            curr_reversed = curr_reversed.next
        return True

    def partition(self, value):
        if self.head is None:
            return
        left = MyLinkedList(None)
        right = MyLinkedList(None)
        curr = self.head

        while curr:
            if curr.data < value:
                left.append(curr.data)
            elif curr.data == value:
                right.insert_to_front(curr.data)
            else:
                right.append(curr.data)
            curr = curr.next

        cur_left = left.head
        if cur_left is None:
            return right
        else:
            while cur_left.next:
                cur_left = cur_left.next
            cur_left.next = right.head
            return left

    def remove_dupes(self):
        if self.head is None:
            return
        prev = self.head
        node = self.head
        seen_data = set()
        while node:
            if node.data not in seen_data:
                seen_data.add(node.data)
                prev = node
                node = node.next
            else:
                prev.next = node.next
                node = node.next

