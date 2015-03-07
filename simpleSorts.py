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
	def selectSort(self):
		for outer in range (0, self.nElems() - 1):
			smallest = outer
			for inner in range (outer + 1, self.nElems()):
				if self.w[inner] < self.w[smallest]:
					smallest = inner
			self.swap(outer, smallest)
	def insertSort(self):
		for outer in range (1, self.nElems()):
			temp = self.w[outer]
			inner = outer
			while inner > 0 and self.w[inner - 1] >= temp:
				self.w[inner] = self.w[inner - 1]
				inner -= 1
			self.w[inner] = temp
	def noDups(self):
		self.insertSort()
		curSwap = 0
		lastKnown = 0
		for i in range (0, self.nElems() - 1):
			if self.w[i] != self.w[i + 1]:
				lastKnown += 1
			elif self.w[i] == self.w[lastKnown]:
				self.w[i] = -1
				lastKnown += 1
		self.display()
		i=0
		while i < self.nElems():
			if self.w[i] == -1:
				self.w.pop(i)
				continue
			i += 1