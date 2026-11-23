class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {} # key -> node

        # doubly linked list
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.nxt = self.right
        self.right.pre = self.left
    def remove(self, node):
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre

    def insert(self, node):
        self.right.pre.nxt = node
        node.pre = self.right.pre
        node.nxt = self.right
        self.right.pre = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.size:
            remove_node = self.left.nxt
            self.remove(remove_node)
            del self.cache[remove_node.key]
        
            
            

        
        
        
