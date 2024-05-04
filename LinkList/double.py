class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.pre = None

class DoublyLinkedList:
    def __init__(self):
         self.head = None

    def insert_at_start(self,data):
        node = Node(data)
        node.pre = None
        node.next = self.head
        self.head = node

    def insert_at_end(self,data):
         node = Node(data)
         if self.head:
             self.head = node
         else:
             current = self.head
         while current:
             current = current.next
         pre_node = current
         node.pre = pre_node
         node.next = None
         pre_node.next = node

    def insert_after(self,pre_node,data):
        if pre_node is None:
            return
        node = Node(data)
        next_node = pre_node.next
        pre_node.next = node
        node.next = next_node
        node.pre = pre_node
        next_node.pre = node

    def insert_before(self,next_node,data):
        if next_node is None:
            return
        node = Node(data)
        pre_node = next_node.pre
        node.pre = pre_node
        node.next = next_node
        pre_node.next = node
        next_node.pre = node   

    def iterative_search(self,key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def recursive_search(self,node,key):
        if not node:
            return False
        if node.data == key:
            return False
        return self.recursive_search(node.next,key)
    
    def iterative_length(self):
        current = self.head
        count = 0
        while current:
           count += 1
           current = current.next
        return count
    
    def recursive_length(self,node):
        if not node:
            return node
        return 1 + self.recursive_length(node.next)
    

    def delete_key(self,key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current.next.pre = None
            current = None
            return
        while current and current.data != key:
            current = current.next
        if current is None:
            return
        temp = current.next
        current.next = temp.next
        if temp.next:
          temp.next.pre = current
        temp = None

    def print_list(self):
        i = self.head
        while i:
            print(i.data)
            i = i.next
            
                




        



