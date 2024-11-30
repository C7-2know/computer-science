class LFUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.freq = 1
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mpp = {}
        self.freq_map = {}
        self.size = 0
        self.min_freq = 0
    
    def deleteNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        # If the frequency list becomes empty, remove it from freq_map
        head, tail = self.freq_map.get(node.freq, (None, None))
        if head and tail and head.next == tail:
            del self.freq_map[node.freq]

    def insertAfterHead(self, node, freq):
        if freq not in self.freq_map:
            head = self.Node(-1, -1) 
            tail = self.Node(-1, -1) 
            head.next = tail
            tail.prev = head
            self.freq_map[freq] = (head, tail)
        head, tail = self.freq_map[freq]
        curNode = head.next
        head.next = node
        node.next = curNode
        curNode.prev = node
        node.prev = head

    def updateFrequency(self, node):
        current_freq = node.freq
        self.deleteNode(node)
        node.freq += 1
        self.insertAfterHead(node, node.freq)
        # If the minimum frequency list becomes empty, update min_freq
        if current_freq == self.min_freq and current_freq not in self.freq_map:
            self.min_freq += 1
        
    def get(self, key: int) -> int:
        if key not in self.mpp:
            return -1
        node = self.mpp[key]
        self.updateFrequency(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.mpp:
            node = self.mpp[key]
            node.val = value
            self.updateFrequency(node)
        else:
            if self.size == self.capacity:
                head, tail = self.freq_map[self.min_freq]
                lru_node = tail.prev
                del self.mpp[lru_node.key]
                self.deleteNode(lru_node)
                self.size -= 1
            node = self.Node(key, value)
            self.mpp[key] = node
            self.insertAfterHead(node, node.freq)
            self.min_freq = 1
            self.size += 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)