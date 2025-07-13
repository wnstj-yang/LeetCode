class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.lru = {}
        self.used = []
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.lru:
            self.used.remove(key)
            self.used.append(key)
            return self.lru[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 1. 존재하면 사용했음
        # 2. 존재안하면 추가,
        if key in self.lru:
            self.lru[key] = value
            self.used.remove(key)
            self.used.append(key)
        else: 
            if len(self.lru) == self.capacity:
                least = self.used[0]
                self.used.remove(least)
                del self.lru[least]
            self.lru[key] = value
            self.used.append(key)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)