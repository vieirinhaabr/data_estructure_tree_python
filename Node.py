class Node(object):
    #ajustar variaveis locais na classe nao globais
    info = None
    esquerdaNode = None 
    direitaNode = None

    def treeNode(self, nodeInfo):
        nonlocal info

        info = nodeInfo

    def insereNode(self, insertValue):
        nonlocal info, esquerdaNode, direitaNode
        print(type(esquerdaNode), "\n")
        if insertValue < info:
            if esquerdaNode is None:
                esquerdaNode = Node()
                esquerdaNode.treeNode(insertValue)
            else:
                esquerdaNode = Node()
                esquerdaNode.insereNode(insertValue)

        elif insertValue > info:
            if direitaNode is None:
                direitaNode = Node()
                direitaNode.treeNode(insertValue)
            else:
                direitaNode = Node()
                direitaNode.insereNode(insertValue)