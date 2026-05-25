class Kerri:
    def __init__(self,emri,shpejtesia):
        self.emri = emri
        self.shpejtesia = shpejtesia

    def printShpejtesine(self):
        print(self.shpejtesia)

    def bbreak(self):
        self.shpejtesia=self.shpejtesia-1

    def rriteShpejtesine(self):
        self.shpejtesia = self.shpejtesia+1
