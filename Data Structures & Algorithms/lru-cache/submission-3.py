class Node:
    def __init__(self,key = None, val = None, next = None, prev = None ) -> None:
        self.next = next
        self.prev = prev
        self.val = val
        self.key= key

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.cap = capacity
        

    def insert(self,key, val):
        new = Node(key, val, self.right, self.right.prev)
        new.prev.next = new
        self.right.prev = new
        self.cache[key] = new

    def remove(self,key):
        curr = self.cache[key]
        curr.prev.next = curr.next
        del self.cache[key]

    def moveToright(self, key):
        curr = self.cache[key]
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr.next = self.right
        curr.prev = self.right.prev
        self.right.prev.next = curr
        self.right.prev = curr

    def get(self, key: int) -> int:
        if key in self.cache:
            self.moveToright(key)
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.moveToright(key)
            self.cache[key].val = value
        else:
            self.insert(key,value)
        if len(self.cache) > self.cap:
            del self.cache[self.left.next.key]
            self.left.next = self.left.next.next
            self.left.next.prev = self.left



