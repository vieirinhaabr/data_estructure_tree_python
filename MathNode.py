class ExpMath(object):
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

    def insertFunc(self, numberOne, numberTwo, operator, id=0):
        if self.numberOne is None:
            self.newFunc(numberOne, numberTwo, operator, id)
        else:
            id += 1
            self.nextFunc = ExpMath()
            self.nextFunc.insertFunc(numberOne, numberTwo, operator, id)

    def countFunc_initializate(self):
        if self.numberOne is not None:
            return 1 + self.countFunc_continue()
        else:
            return 0

    def countFunc_continue(self):
        if self.nextFunc is not None:
            return 1 + self.nextFunc.countFunc_continue()
        else:
            return 0

    def returnExp(self, id):
        if self.id == id:
            return self.operator, self.numberOne, self.numberTwo
        else:
            if self.nextFunc is not None:
                return self.nextFunc.returnExp(id)
            else:
                print("error when trying to find function")
                return 'empty'