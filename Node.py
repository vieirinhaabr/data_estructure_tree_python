class Node(object):
    #ajustar variaveis locais na classe nao globais
    info = None
    esquerdaNode = None
    direitaNode = None

    def treeNode(self, nodeInfo):
        self.info = nodeInfo
        print(Node.info, "inserido Node Class")

    def insereNode(self, insertValue):
        print("\n",self.info, " NODE ENTRADA INSERE\n")
        print("\n",type(self.esquerdaNode), " TYPE NODE ESQUERDA\n")
        if insertValue < self.info:
            if self.esquerdaNode is None:
                self.esquerdaNode = Node()
                print(type(self.esquerdaNode), "TYPE ESQUERDA NODE POS DEFICINICAO NODE()")
                self.esquerdaNode.treeNode(insertValue)
                print(self.esquerdaNode.info, "ESQUERDA NODE INFO")
                print(self.info)
            else:
                self.esquerdaNode.insereNode(insertValue)

        elif insertValue > self.info:
            if self.direitaNode is None:
                self.direitaNode = Node()
                print(type(self.direitaNode), "TYPE DIREITA NODE POS DEFICINICAO NODE()")
                self.direitaNode.treeNode(insertValue)
                print(self.direitaNode.info, "DIREITA NODE INFO")
                print(self.info)
            else:
                self.direitaNode.insereNode(insertValue)