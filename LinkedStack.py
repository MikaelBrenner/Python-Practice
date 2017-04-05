class LinkedStack:
    '''A linked list based implemention of a Stack data structure      
       -Mikael Brenner, 2017'''
    class _Node:
        #Non-public class to create the Nodes that the structure is based upon'''
        __slots__ = '_element','_nextelement'   #Create the space in the memory to the Nodes
        def __init__(self,element,nextelement):
            #Initialize a new $Node
            self._element = element
            self._nextelement = nextelement

    def __init__(self):
        #Initialize
        self._head = None
        self._size = 0

    def __len__(self):
        #Return the size of the stack based on the number of elements 
        return self._size

    def is_empty(self):
        #Test if the stack is empty using the counter of elements
        return self._size == 0

    def push(self,e):
        #Adds an element to the top of the stack
        self._head = self._Node(e,self._head)  #Creates a new Node to store the new element
        self._size += 1

    def top(self):
        #Returns the top element without removing it from the stack
        if self.is_empty():
            raise ValueError('List is empty') #Refuses to do it on a empty stack
        return self._head._element

    def pop(self):
        #Removes the top element of the stack and return it
        if self.is_empty():
            raise ValueError('List is empty')  #Refuses to do it on a empty list
        temp = self._head._element
        self._head = self._head._nextelement    #Updates the head Node
        self._size -= 1
        return temp

if __name__ == '__main__':
    #Tests
    test = LinkedStack()
    for i in range(12):
        test.push(i)
    for k in range(5):
        print(test.pop())
    print(test.top())
    print("Everything is okay!")
