class Node(object):
    #ajustar variaveis locais na classe nao globais
    info = None
    esquerdaNode = None
    direitaNode = None

    def treeNode(self, nodeInfo):
        self.info = nodeInfo

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