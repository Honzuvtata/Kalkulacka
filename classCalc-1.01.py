class Calc():
    def __init__(self):
        self.cislo1 = 0
        self.cislo2 = 0
        self.cislo3 = 0
        self.cislo4 = 0
        self.numberOrder = 1
        self.numberMemory = []



    def secti(self):
        return (self.numberMemory[self.numberOrder - 1] + self.numberMemory[self.numberOrder])

    def odecti(self):
        return(self.numberMemory[self.numberOrder - 1] - self.numberMemory[self.numberOrder])

    def vynasob(self):
        return(self.numberMemory[self.numberOrder - 1] * self.numberMemory[self.numberOrder])

    def vydel(self):
        return(self.numberMemory[self.numberOrder - 1] / self.numberMemory[self.numberOrder])

calc = Calc()

calc.numberMemory.append(10)

calc.numberMemory.append(5)

print(calc.secti())

print(calc.odecti())

print(calc.vynasob())

print(calc.vydel())
