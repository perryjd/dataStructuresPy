class bubArray:
	def __init__(self):
		self.w = []
	def insert(self, value):
		self.w.append(value)
	def display(self):
		print self.w
	def swap(self, first, second):
		temp = self.w[first]
		self.w[first] = self.w[second]
		self.w[second] = temp
	def nElems(self):
		return len(self.w)
	def bubbleSort(self):
		for outer in range (self.nElems() - 1, 0, -1):
			for inner in range (0, outer):
				 if self.w[inner] > self.w[inner + 1]:
				 	self.swap(inner, inner + 1)

myArray = bubArray()
for x in range (10, -1, -1):
	myArray.insert(x)

myArray.display()

myArray.bubbleSort()

myArray.display()