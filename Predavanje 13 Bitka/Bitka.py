import risar

from random import randint


class Krog:
    def __init__(self, r) -> None:
        self.x = risar.nakljucne_koordinate()[0]
        self.y = risar.nakljucne_koordinate()[1]
        self.r = 10
        self.barva = risar.nakljucna_barva()
        self.krog = risar.krog(self.x, self.y, self.r, self.barva, sirina=1)
        self.krog.setPos(self.x, self.y)
        self.xs = 5
        self.ys = 5

    def premik(self):
        self.x = self.x + self.xs
        self.y = self.y + self.ys
        if self.x + 20 >= risar.maxx or self.x <= 0:
            self.xs = -self.xs
        if self.y + 20 >= risar.maxy or self.y <= 0:
            self.ys = -self.ys
        self.krog.setPos(self.x,self.y)


vsi = []
for i in range(30):
    vsi.append(Krog(10))
t = 0
while t <= 20:
    for krog in vsi:
        krog.premik()
    risar.cakaj(0.02)
    t += 0.03

#Vse ladje naj se premikajo z enako hitrostjo, namreč 5 točk na eno iteracijo zanke;
# v zanko dodajte 0.02 sekunde pavze. (Namig: za x-komponento hitrosti določite naključno število med -5 in 5.
# Komponento y izračunate po Pitagori. V polovici primerov jo obrnite pozitivno, v polovici negativno.)

