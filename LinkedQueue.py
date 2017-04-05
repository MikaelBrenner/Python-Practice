class LinkedQueue:
    '''A linked list based of the Queue data structure
    -Mikael Brenner,2017'''
    class _Node:
        #Non-public class to create the nodes to store the elements
        __slots__ = '_element','_nextelement' #Define the usage of memory by the nodes

        def __init__(self,element,nextelement):
            #Initialize a new Node
            self._element = element
            self._nextelement = nextelement

    def __init__(self):
        #Initialize a new Queue
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        #Uses the counter to show the size of the Queue
        return self._size

    def is_empty(self):
        #Uses the counter to show if the Queue is empty
        return self._size == 0

    def first(self):
        #Returns the first element of the Queue without removing it
        if self.is_empty():
            raise ValueError("Empty Queue")
        return self._head._element

    def enqueue(self,new_element):
        #Adds a new element to the Queue
        if new_element == None:
            raise ValueError("Can't enqueue nothing!")  #Refuses to add None to the Queue
        if self.is_empty(): #Deals with the first element enqueued
            self._head = self._Node(new_element,self._head)
            self._tail = self._head
        else:
            self._tail._nextelement = self._Node(new_element,None) #Creates a new Node to store the new element
        self._size += 1

    def dequeue(self):
        #Removes the first element of the Queue,returning it
        if self.is_empty():
            raise ValueError("Queue is empty")  #Deals with dequeue requests on empty Queues
        temp_head = self._head._element  #Stores the current head
        self._head = self._head._nextelement  #Updates the head
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return temp_head

if __name__ == '__main__':
    #Tests
    test = LinkedQueue()
    test.is_empty()
    for i in range(12):
        test.enqueue(i)
    for k in range(5):
        print(test.dequeue())
    print(test.first())
    print("Everything is okay!")


