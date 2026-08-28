class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_mapping = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt,prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.key_mapping:
            node = self.key_mapping[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.key_mapping:
            self.key_mapping[key].val = value
            self.remove(self.key_mapping[key])
            self.insert(self.key_mapping[key])
            return

        newNode = Node(value, key)
        if len(self.key_mapping) >= self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.key_mapping[lru.key]
        self.insert(newNode)
        self.key_mapping[key] = newNode

        return
        

        
