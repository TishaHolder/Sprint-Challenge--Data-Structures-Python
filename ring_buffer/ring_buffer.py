from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()       
       

    def append(self, item):

        #if the list is empty
        if self.storage.length == 0:

            #add the item to the head of the list
            self.storage.add_to_head(item)

            #set it as the head of the ring buffer
            self.current = self.storage.head
            

        #if self.current is at the head and the ring buffer is full
        elif self.storage.length == self.capacity and self.current is self.storage.head:

            #remove from the head
            self.storage.remove_from_head()

            #add the new item to the tail
            self.storage.add_to_tail(item)

            #set the item at the tail as the head of the list
            self.current = self.storage.tail

        
        #if not at capacity
        else:
            #add the item to the tail  
            self.storage.add_to_tail(item)           
    
            

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
       

        return list_buffer_contents   


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass