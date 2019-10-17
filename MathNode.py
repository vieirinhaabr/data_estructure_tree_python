class FuncCalc(object):
    numberOne = None
    numberTwo = None
    operator = None
    nextFunc = None
    id = 0

    def newFunc(self, numberOne, numberTwo, operator, id):
        self.numberOne = numberOne
        self.numberTwo = numberTwo
        self.operator = operator
        self.id = id

    def inserirFunc(self, numberOne, numberTwo, operator, id=0):
        if self.numberOne is None:
            self.newFunc(numberOne, numberTwo, operator, id)
        else:
            id += 1
            self.nextFunc = FuncCalc()
            self.nextFunc.inserirFunc(numberOne, numberTwo, operator, id)

    def contarFunc(self):
        if self.numberOne != None:
            return 1 + self.contarFuncDivs()
        else:
            return 0
    
    def contarFuncDivs(self):
        if self.nextFunc != None:
            return 1 + self.nextFunc.contarFuncDivs()
        else:
            return 0
    
    def returnExp(self, id):
        if self.id == id:
            return (self.operator, self.numberOne, self.numberTwo)
        else:
            if nextFunc != None:
                self.nextFunc.returnExp(id)
            else:
                print("erro ao encontrar função")
                return ('empty')