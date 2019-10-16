from Node import Node

class Tree(object):

    raiz = None

    def insereNode(self, insertValue):
        if self.raiz is None:
            self.raiz = Node()
            self.raiz.treeNode(insertValue)
        else:
            self.raiz.insereNode(insertValue)

    def preorderTraversal(self):
        self.preorderHelper(self.raiz)

    def preorderHelper(self, node):
        if node is None:
            return

        print(node.info, " , ", end = '')

        self.preorderHelper(node.esquerdaNode)

        self.preorderHelper(node.direitaNode)

    def inorderTraversal(self):
        self.inorderHelper(self.raiz)

    def inorderHelper(self, node):
        if node is None:
            return

        self.preorderHelper(node.esquerdaNode)

        print(node.info, " , ", end = '')

        self.preorderHelper(node.direitaNode)

    def postorderTraversal(self):
        self.postorderHelper(self.raiz)

    def postorderHelper(self, node):
        if node is None:
            return

        self.preorderHelper(node.esquerdaNode)

        self.preorderHelper(node.direitaNode)

        print(node.info, " , ", end = '')