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