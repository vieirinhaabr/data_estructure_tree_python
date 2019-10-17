class Node(object):
    #ajustar variaveis locais na classe nao globais
    info = None
    esquerdaNode = None
    direitaNode = None

    def treeNode(self, nodeInfo):
        self.info = nodeInfo

    def expression_Node(self, truple_expression):
        self.esquerdaNode = Node()
        self.direitaNode = Node()
        self.info = truple_expression[0]
        self.esquerdaNode.info = truple_expression[1]
        self.direitaNode.info = truple_expression[2]

    def insereNode(self, insertValue):
        if insertValue < self.info:
            if self.esquerdaNode is None:
                self.esquerdaNode = Node()
                self.esquerdaNode.treeNode(insertValue)
            else:
                self.esquerdaNode.insereNode(insertValue)

        elif insertValue > self.info:
            if self.direitaNode is None:
                self.direitaNode = Node()
                self.direitaNode.treeNode(insertValue)
            else:
                self.direitaNode.insereNode(insertValue)

    def insereNode_Expression_Esquerda(self, truple_expression):
        if self.esquerdaNode is None:
            self.esquerdaNode = Node()
            self.esquerdaNode.expression_Node(truple_expression)
        else:
            self.esquerdaNode.insereNode_Expression_Esquerda(truple_expression)

    def insereNode_Expression_Direita(self, truple_expression):
        if self.direitaNode is None:
            self.direitaNode = Node()
            self.direitaNode.expression_Node(truple_expression)
        else:
            self.direitaNode.insereNode_Expression_Direita(truple_expression)