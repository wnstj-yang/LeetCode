# # 1. 단순 풀이(문제 그대로 이해진행)
# class LRUCache(object):

#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.capacity = capacity
#         self.lru = {}
#         self.used = []
        

#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key in self.lru:
#             self.used.remove(key)
#             self.used.append(key)
#             return self.lru[key]
#         else:
#             return -1
        

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         # 1. 존재하면 사용했음
#         # 2. 존재안하면 추가,
#         if key in self.lru:
#             self.lru[key] = value
#             self.used.remove(key)
#             self.used.append(key)
#         else: 
#             if len(self.lru) == self.capacity:
#                 least = self.used[0]
#                 self.used.remove(least)
#                 del self.lru[least]
#             self.lru[key] = value
#             self.used.append(key)

        
# 2. 이중 연결리스트 활용하기
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.cache = {} # 노드의 정보 캐싱
        self.capacity = capacity
    
    # 접근
    def get(self, key):
        if key not in self.cache:
            return -1
        # 캐싱이 되어있으면 이중연결리스트에 대한 순서 변경
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.value

    # 추가
    def put(self, key, value):
        if key in self.cache:
            # 기존 노드 제거
            self.remove(self.cache[key])
        
        # 새 노드 생성 및 추가
        new_node = Node(key, value)
        self.add(new_node)
        self.cache[key] = new_node

        # 용량 초과 시 LRU 제거
        if len(self.cache) > self.capacity:
            lru_node = self.head
            self.remove(lru_node)
            del self.cache[lru_node.key]

    def add(self, node):
        # 중간에 지워지고 다시 추가되는 경우 + 단순 추가 => self.tail 판단
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        else:
            # tail이 없으면 머리통인 head도 추가된다.
            self.head = node
        self.tail = node
        node.next = None # 새로 추가된 경우이므로 next도 None으로 초기화
        

    def remove(self, node):
        # 노드의 prev, next 파악하여 연결
        if node.prev:
            # 있으면 연결시켜줌
            node.prev.next = node.next
        else:
            # 없으면 head를 갱신 
            self.head = node.next 
        
        if node.next:
            # 있으면 연결
            node.next.prev = node.prev
        else:
            # 없으면 tail 갱신
            self.tail = node.prev



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)