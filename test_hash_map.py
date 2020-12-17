import unittest


class Item(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return key % self.size

    def set(self, key, value):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))

    def get(self, key):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError('key not found')

    def remove(self, key):
        hash_index = self._hash_function(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return
        raise KeyError('Key not found')


class MyTestCase(unittest.TestCase):

    def test_end_to_end(self):
        hash_table = HashTable(10)

        print("Test: get on an empty hash table index")

        self.assertRaises(KeyError, hash_table.get, 0)

        print("Test: set on an empty hash table index")

        hash_table.set(0, 'foo')

        self.assertEqual(hash_table.get(0), 'foo')

        hash_table.set(1, 'bar')

        self.assertEqual(hash_table.get(1), 'bar')

        print("Test: set on a non empty hash table index")

        hash_table.set(10, 'foo2')

        self.assertEqual(hash_table.get(0), 'foo')

        self.assertEqual(hash_table.get(10), 'foo2')

        print("Test: set on a key that already exists")

        hash_table.set(10, 'foo3')

        self.assertEqual(hash_table.get(0), 'foo')

        self.assertEqual(hash_table.get(10), 'foo3')

        print("Test: remove on a key that already exists")

        hash_table.remove(10)

        self.assertEqual(hash_table.get(0), 'foo')

        self.assertRaises(KeyError, hash_table.get, 10)

        print("Test: remove on a key that doesn't exist")

        self.assertRaises(KeyError, hash_table.remove, -1)

        print('Success: test_end_to_end')


if __name__ == '__main__':
    unittest.main()
