class Stack:
	'''A list based implemention of the Stack data structure
	-Mikael Brenner,2017'''
	def __init__(self):
		#Initialize
		self._list = []		#List used to store the data
		self._n = 0			#Counter to store number of elements in the list
		self._top = None	#Stores the element at the top of the stack for fast reference

	def __len__(self):
		#Uses the number of elements as lenght
		return self._n    

	def __repr__(self):
		#Format the Stack to be printed
		st = ''
		for k in self._list[::-1]:
			st += '||{0}||\n'.format(k)
		return st

	def is_empty(self):
		#Uses the counter to test
		return self._n == 0		

	def top(self):
		return self._top	

	def push(self,element):
		#Add an element to the stack
		self._list.append(element)
		self._n += 1
		self._top = element

	def pop(self):
		#Return the top element,removing it from the stack
		if self.is_empty():		
			return 'Stack is empty' 	#Refuses to pop something from a empty list
		else:
			return self._list.pop()		#Uses the built-in pop method of the class list