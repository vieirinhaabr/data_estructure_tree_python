class FuncCalc(object):
    numberOne = None
    numberTwo = None
    operator = None
    nextFunc = None

    def newFunc(self, numberOne, numberTwo, operator):
        self.numberOne = numberOne
        self.numberTwo = numberTwo
        self.operator = operator

    def inserirFunc(self, numberOne, numberTwo, operator):
        if self.numberOne is None:
            self.newFunc(numberOne, numberTwo, operator)
        else:
            self.nextFunc = FuncCalc()
            self.nextFunc.inserirFunc(numberOne, numberTwo, operator)

    def contarFunc(self, id=0):
        self.contarFunc().contarFuncDivs(id)
        def contarFuncDivs(id):
            if self.numberOne != None:
                id += 1
                self.nextFunc.contarFunc()
            else:
                return id
            
        return id