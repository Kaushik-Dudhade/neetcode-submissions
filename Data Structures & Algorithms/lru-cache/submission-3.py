class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}

        self.left,self.right = Node(0,0), Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if not key in self.map:
            return -1

        self.remove(self.map[key])
        self.insert(self.map[key])

        return self.map[key].value
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        
        self.map[key] = Node(key,value)
        self.insert(self.map[key])
        
        if len(self.map) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.map[lru.key]
        
    
    def remove(self,node):
        prv,nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv
    
    def insert(self,node):
        prev,nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt
    
