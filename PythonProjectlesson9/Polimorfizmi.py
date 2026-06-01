class Kafsha():
    def __init__(self,emri):
        self.emri = emri

    def tingulli(self):
        print("Kafsha ben nje tingull")

class Maca(Kafsha):

    def tingulli(self):
        print("Kafsha ben nje tingull")



class Qeni(Kafsha):

    def tingulli(self):
        print("hammmmhammmm")



kafsha1=Kafsha("xkafsha")
kafsha1.tingulli()

qeni=Qeni("bobi")
qeni.tingulli()

maca=Maca("jddkjd")
maca.tingulli()