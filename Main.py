
from Tree import Tree

if __name__ == "__main__":

	Tree = Tree()

	Tree.resolveMath(question='3*5+5/5')
	Tree.criarTree()

	"""print("Inserting Tree ...")
	Tree.insertNode(7)
	Tree.insertNode(6)
	Tree.insertNode(5)
	Tree.insertNode(4)
	Tree.insertNode(25)
	Tree.insertNode(2)
	Tree.insertNode(88)
	Tree.insertNode(55)
	Tree.insertNode(99)"""

	print("\ninorderTraversal \n")
	print("Tree ", end='')
	Tree.inorderTraversal()