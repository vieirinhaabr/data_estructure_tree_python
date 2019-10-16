from Node import Node
from MathNode import FuncCalc

class Tree(object):

    raiz = None
    sepFunc = None
    numberOne = None
    numberTwo = None
    operator = None
    funcRaiz = None

    def insereNode(self, insertValue):
        if self.raiz is None:
            self.raiz = Node()
            self.raiz.treeNode(insertValue)
        else:
            self.raiz.insereNode(insertValue)

    """def preorderTraversal(self):
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

        print(node.info, " , ", end = '')"""

    #(3+5)+(5+5)

    def resolveMath(self, question):
        status = False
        self.funcRaiz = FuncCalc()

        midQuestion = int(len(question) / 2)
        
        self.raiz = question[midQuestion]

        for thing in question:
            if thing != self.raiz:
                status = True
            elif thing == self.raiz:
                status = False
                self.funcRaiz.inserirFunc(self.numberOne, self.numberTwo, self.operator)
                self.numberOne = None
                self.numberTwo = None
                self.operator = None
            if status == True:
                if (thing != '+') and (thing != '-') and (thing != '*') and (thing != '/'):
                    if self.numberOne is None:
                        self.numberOne = thing
                    else:
                        self.numberTwo = thing
                else:
                    self.operator = thing
        if status == True:
            status = False
            self.funcRaiz.inserirFunc(self.numberOne, self.numberTwo, self.operator)
            self.numberOne = None
            self.numberTwo = None
            self.operator = None
        
        print(self.funcRaiz.numberOne, self.funcRaiz.operator, self.funcRaiz.numberTwo)

    def passarMathtoNode():
        print(self.funcRaiz.contarFunc())