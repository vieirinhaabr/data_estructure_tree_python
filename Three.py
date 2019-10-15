from Node import Node

#nao cria novo node, tem que por na funcao
node = Node()
raiz = None

class Three(object):

    def insereNode(self, insertValue):
        global raiz
        global node

        if raiz is None:
            raiz = Node()
            raiz.treeNode(insertValue)
            print(insertValue, "inserido na raiz")
        else:
            raiz.insereNode(insertValue)
            print(insertValue, "inserido")

    def preorderTraversal(self):
        global raiz

        self.preorderHelper(raiz)

    def preorderHelper(self, node):
        if node is None:
            return

        print(node.info + " , ")

        self.preorderHelper(node.esquerdaNode)

        self.preorderHelper(node.direitaNode)

    def inorderTraversal(self):
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

        System.out.print(node.info + " , ")