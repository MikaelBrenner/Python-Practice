class Queue:
	'''A list based implemention of the Queue data structure
	-Mikael Brenner,2017'''
	def __init__(self):
		#Initialization
		self._list = []		#Stores the data
		self._n = 0 		#Count the number of elements in the list
		self._first = None 	#Stores the first element for fast reference
		self._first_location = 0	#Stores the location of the fist element
	
	def __len__(self):
		#Uses the built-in __len__ method on the list that stores our data
		return len(self._list)	

	def __repr__(self):
		#Beautify the Queue for printing
		listrpr = ['{0}|'.format(x) for x in self._list if x != None]		#Uses list comprehension to avoiding to display empty cells
		rpr = ''.join(listrpr)
		return rpr	

	def _refresh_first(self):	
		#Does precisely what the name says
		for k in self._list:
			if k != None:
				return k

	def _resize(self):	
		#Shrink the list to avoid storing too many empty cells
		pivot = self._refresh_first()   #Get the first element that's not a None
		location = self._list.index(pivot)	#And its index
		self._list = self._list[location:]	#Use list slicing to cut the empty out
		self._first = self._list[0]				#restore the positioning
		self._first_location = 0

	def is_empty(self):
		#Uses the counter that stores the number of elements in the Queue
		return self._n == 0

	def first(self):
		return self._first  

	def enqueue(self,nw):
		#Function that adds members to the Queue
		if nw == None:
			raise ValueError("Can't enqueue nothing!")  #Refuses enqueue requests for None objects
		self._list.append(nw)	#Enqueue the received value
		self._n += 1			#Increase the number of elements
		if self._first == None:		#Deals with the first enqueued object
			self._first = nw
			self._first_location = 0

	def dequeue(self):
		#Function that advance the Queue,taking the first member out
		temp_first = self._first    #Stores the current value of first,because it will be changed
		self._list[self._first_location] = None		#Change the value previously stored to None
		self._n -= 1		
		if self._n <= (len(self) / 2):		#In the case tat Nones make up to more than half of the list,shrink the list
			self._resize()
		self._first = self._refresh_first()		#Get the new list first element
		self._first_location = self._list.index(self._first)	#Re-set the location variable
		return temp_first

if __name__ == '__main__':
	#Tests
	test = Queue()
	test.is_empty()
	for i in range(12):
        test.enqueue(i)
    for k in range(5):
        print(test.dequeue())
    print(test.first())
    print("Everything is okay!")
 