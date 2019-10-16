from Tree import Tree

if __name__ == "__main__":
    Arvore = Tree()

    print("Inserindo Arvore ...")
    Arvore.insereNode(7)
    Arvore.insereNode(6)
    Arvore.insereNode(5)
    Arvore.insereNode(4)
    Arvore.insereNode(25)
    Arvore.insereNode(2)
    Arvore.insereNode(88)
    Arvore.insereNode(55)
    Arvore.insereNode(99)

    print("inorderTraversal \n")
    print("Arvore ", end='')
    Arvore.inorderTraversal()