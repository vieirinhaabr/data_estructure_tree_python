from Node import Node

class Tree(object):

    raiz = None

    def insereNode(self, insertValue):
        if self.raiz is None:
            self.raiz = Node()
            self.raiz.treeNode(insertValue)
            print(insertValue, "inserido na raiz TREE")
        else:
            self.raiz.insereNode(insertValue)
            print(insertValue, "inserido TREE")

    def preorderTraversal(self):
        self.preorderHelper(self.raiz)

    def preorderHelper(self, node):
        if node is None:
            return

        print(node.info, " , ")

        self.preorderHelper(node.esquerdaNode)

        self.preorderHelper(node.direitaNode)

    """def inorderTraversal(self):
        global raiz

        inorderHelper(raiz)

    def inorderHelper(self, node):
        if node is None:
            return

        inorderHelper(node.esquerdaNode)

        System.out.print(node.info + " , ")

        inorderHelper(node.direitaNode)

    def postorderTraversal(self):
        global raiz

        postorderHelper(raiz)

    def postorderHelper(self, node):
        if node is None:
            return

        postorderHelper(node.esquerdaNode)

        postorderHelper(node.direitaNode)

        System.out.print(node.info + " , ")"""