from Node import Node
from MathNode import ExpMath


class Tree(object):
    root = None
    numberOne = None
    numberTwo = None
    operator = None
    funcroot = None

    """def insertNode(self, insertValue):
        if self.root is None:
            self.root = Node()
            self.root.treeNode(insertValue)
        else:
            self.root.insertNode(insertValue)

    def preorderTraversal(self):
        self.preorderHelper(self.root)

    def preorderHelper(self, node):
        if node is None:
            return

        print(node.info, " , ", end = '')

        self.preorderHelper(node.leftNode)

        self.preorderHelper(node.rightNode)"""

    def inorderTraversal(self):
        self.inorderHelper(self.root)

    def inorderHelper(self, node):
        if node is None:
            return

        self.inorderHelper(node.leftNode)

        print(node.info, " , ", end = '')

        self.inorderHelper(node.rightNode)

    """def postorderTraversal(self):
        self.postorderHelper(self.root)

    def postorderHelper(self, node):
        if node is None:
            return

        self.postorderHelper(node.leftNode)

        self.postorderHelper(node.rightNode)

        print(node.info, " , ", end = '')"""

    # (3+5)+(5+5)

    def resolveMath(self, question):
        status = False

        self.funcroot = ExpMath()
        self.root = Node()

        midQuestion = int(len(question) / 2)
        self.root.info = question[midQuestion]

        for thing in question:
            if thing == self.root.info:
                status = False
                self.insert_math()
            else:
                status = True
            if status:
                if (thing != '+') and (thing != '-') and (thing != '*') and (thing != '/'):
                    if self.numberOne is None:
                        self.numberOne = thing
                    else:
                        self.numberTwo = thing
                else:
                    self.operator = thing
        if status:
            self.insert_math()

    def insert_math(self):
        self.funcroot.insertFunc(self.numberOne, self.numberTwo, self.operator)
        self.numberOne = None
        self.numberTwo = None
        self.operator = None

    def criarTree(self):
        if self.funcroot.countFunc_initializate() == 0:
            print("No operation entrance")
        else:
            if self.root is None:
                print("Root dont find")
            else:
                count_right = int(self.funcroot.countFunc_initializate())

                count_left = int(count_right / 2)
                i = 0
                while i < count_left:
                    truple_exp = self.funcroot.returnExp(i)
                    if truple_exp != 'empty':
                        self.root.insertNode_Expression_left(truple_exp)
                        print("Expression transformed in Node -> Successful")
                    i = + 1

                i = count_left
                while i < count_right:
                    truple_exp = self.funcroot.returnExp(i)
                    if truple_exp != 'empty':
                        self.root.insertNode_Expression_right(truple_exp)
                        print("Expression transformed in Node -> Successful")
                    i = i + 1