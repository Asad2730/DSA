class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
         self.head = None


    def insert_at_start(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        else:
            node.next = self.head
            self.head = node

    def insert_at_end(self, data):
      node = Node(data)
      if not self.head:
        self.head = node
      else:
             current = self.head
             while current.next:
              current =  current.next
             current.next = node       
    

    def insert_after(self,pre_node,data):
        if pre_node is None:
            return
        node = Node(data)
        node.next = pre_node.next
        pre_node.next = node

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
            return True
        return self.recursive_search(node.next,key)
    
    def iterative_length(self):
         current = self.head
         size = 0
         while current:
             size += 1
             current = current.next
         return size

    def recursive_length(self,node):
          if not node:
              return 0
          return 1 + self.recursive_length(node.next)

    def reverse(self):
        prev = None
        current = self.head
        while current:
          node = current.next
          current.next = prev
          prev = node
          current = node
        self.head = prev

    def delete_key(self, key):
        current = self.head
        if current and current.data == key:
             self.head = current.next
             current = None
             return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None           
    
    def delete_list(self):
        current = self.head
        while current:
            next_node = current.next
            del current.data
            current = next_node
        self.head = None

    def delete_position(self, position):
         if self.head:
             temp = self.head
             if position == 0:
                 self.head = temp.next
                 temp = None
                 return
             for i in range(position-1):
                 temp = temp.next
                 if temp is None:
                     break
             if temp is None:
                 return
             if temp.next is None:
                 return
             node = temp.next.next
             temp.next = None
             temp.next = node        

    def print_list(self):
        i = self.head
        while i:
            print(i.data)
            i = i.next      