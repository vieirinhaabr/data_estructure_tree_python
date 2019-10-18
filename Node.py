class Node(object):
	info = None
	leftNode = None
	rightNode = None

	def treeNode(self, nodeInfo):
		self.info = nodeInfo

	def insertNode(self, insertValue):
		if insertValue < self.info:
			if self.leftNode is None:
				self.leftNode = Node()
				self.leftNode.treeNode(insertValue)
			else:
				self.leftNode.insertNode(insertValue)

		elif insertValue > self.info:
			if self.rightNode is None:
				self.rightNode = Node()
				self.rightNode.treeNode(insertValue)
			else:
				self.rightNode.insertNode(insertValue)

	def expression_Node(self, truple_expression):
		self.leftNode = Node()
		self.rightNode = Node()
		self.info = truple_expression[0]
		self.leftNode.info = truple_expression[1]
		self.rightNode.info = truple_expression[2]

	def insertNode_Expression_left(self, truple_expression):
		if self.leftNode is None:
			self.leftNode = Node()
			self.leftNode.expression_Node(truple_expression)
		else:
			self.leftNode.insertNode_Expression_left(truple_expression)

	def insertNode_Expression_right(self, truple_expression):
		if self.rightNode is None:
			self.rightNode = Node()
			self.rightNode.expression_Node(truple_expression)
		else:
			self.rightNode.insertNode_Expression_right(truple_expression)