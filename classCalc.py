class Calc():
    def __init__(self):
        self.cislo1 = 0
        self.cislo2 = 0
        self.cislo3 = 0
        self.cislo4 = 0
        self.numberOrder = 1
        self.numberMemory = [1, 5]



    def secti(self):
        return (self.numberMemory[self.numberOrder - 1] + self.numberMemory[self.numberOrder])

    def odecti(self):
        return(self.numberMemory[self.numberOrder - 1] - self.numberMemory[self.numberOrder])

calc = Calc()

calc.cislo1 = 1

calc.cislo2 = 2

print(calc.secti())

print(calc.odecti())
