import heapq


class QueueNode(object):

    def __init__(self, obj, key):
        self.obj = obj
        self.key = key

    def __repr__(self):
        return str(self.obj) + ': ' + str(self.key)

    def __lt__(self, other):
        return self.key < other.key

class PriorityQueue(object):

    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def insert(self, node):
        # self.array.append(node)
        # return self.array[-1]
        return heapq.heappush(self.array, node)

    def extract_min(self):
        if not self.array:
            return None
        # min = sys.maxsize
        # for index, node in enumerate(self.array):
        #     if node.key < min:
        #         min = node.key
        #         min_index = index
        # return self.array.pop(min_index)
        return heapq.heappop(self.array)

    def decrease_key(self, obj, new_key):
        for node in self.array:
            if node.obj is obj:
                node.key = new_key
                return None
        return None
