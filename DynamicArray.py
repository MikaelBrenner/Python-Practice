import ctypes
class DynamicArray:
	'''A C array based implementation of a dynamic array mimicking 
		 the built-in List class    -Mikael Brenner, 2017'''
	def __init__(self):
		#Initialize
		self._n = 0			#Counts the number of elements on the array
		self._capacity = 1	#Initial capacity
		self._A = self._make_array(self._capacity)	#Create the C array

	def __len__(self):
		#Uses the counter to get the lenght
		return self._n

	def __getitem__(self,i):
		#Deals with requests for elements by index
		if i > self._n:
			raise IndexError("Index out of range")	#Deals with OOR error
		if  0 <= i < self._n:
			return self._A[i]			#Normal access by index
		if i < 0  and 0 <= abs(i) <= self._n:
			return self._A[(self._n + i)]		#Backwards access for negative index
			
	def append(self,obj):
		#Add an element to the array
		if self._n == self._capacity:
			self._resize(2* self._capacity)		#Double the size of the array if it's full
		self._A[self._n] = obj
		self._n += 1

	def pop(self):
		#Get the last element
		self._A[-1] = None
		self._n -= 1		
		if self._n <= (self._capacity / 4):
			self._resize(-1)			#Shrinks the array if there are too many empty seats

	def _resize(self,c):
		#Changes the size of the array to keep a good size at the memory
		if c == -1:
			C = self._make_array(self._capacity / 2)
			for j in range(self._n):
				C[j] = self._A[j]
			self._A = C
			self._capacity = self._capacity / 2
		else:
			B = self._make_array(c)
			for k in range(self._n):
				B[k] = self._A[k]
			self._A = B
			self._capacity = c

	def _make_array(self,c):
		#Creates the C array
		return (c*ctypes.py_object)()
