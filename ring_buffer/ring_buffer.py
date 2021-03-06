from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        #doesn't need a size, non-growable fixed size buffer or capacity is passed in during instantiation
        self.capacity = capacity
        self.current = None #used to keep track of the oldest element
        self.storage = DoublyLinkedList()       
       

    def append(self, item):

        #if the list is empty
        if self.storage.length == 0:

            #add the item to the head of the list
            self.storage.add_to_head(item)

            #set it as the current item
            self.current = self.storage.head            

        #if self.current is at the head and the ring buffer is full
        elif self.storage.length == self.capacity and self.current is self.storage.head:

            #remove from the head
            self.storage.remove_from_head()

            #add the new item to the tail
            self.storage.add_to_tail(item)

            #set the item at the tail as the current item
            #have to update self.current as it was removed from the head
            self.current = self.storage.tail

        #if self.current is not at the head and the ring buffer is full
        elif self.storage.length == self.capacity and self.current is not self.storage.head:

            #remove the item from the head
            self.storage.remove_from_head()

            #add the new item to the tail
            self.storage.add_to_tail(item)     

            #no need to update self.current as it was not removed (it was not at the head)       

        #if not at capacity
        else:
            #add the item to the tail  
            self.storage.add_to_tail(item)       
            
            #no need to update self.current here either as it was not removed

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
       

        #while not all the ring buffer's content is in list_buffer_contents
        while self.storage.length != len(list_buffer_contents):

            #add the current value in storage to the list_buffer_contents
            list_buffer_contents.append(self.current.value) 

            #if there is more than one item in the list
            #assign it to current and append it to list_buffer_contents
            if self.current.next:
                self.current = self.current.next  

            #else assign the head node to current to be appended to list_buffer_contents
            else:
                self.current = self.storage.head                  
            

        return list_buffer_contents   


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass