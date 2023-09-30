import unittest
from collections import defaultdict

def preberi_pravokotnike(ime_datoteke):
    # moja resitev
    # seznam = []
    # nov = []
    # for v in open(ime_datoteke):
    #     for terka in v.split("-"):
    #         # Tako lahko appendamo vse elemente ki jih dobimo iz zanke
    #         seznam.append(tuple(int(st) for st in terka.strip().split(",")))
    # i = 0
    # while i < len(seznam):
    #     nov.append(seznam[i] + seznam[i + 1])
    #     i += 2
    # return nov
    sez = []
    for v in open(ime_datoteke):
        koord1, koord2 = v.strip().split("-")
        x1,y1 = koord1.strip().split(",")
        x2, y2 = koord2.strip().split(",")
        sez.append((int(x1),int(y1),int(x2),int(y2)))

    return sez


def nepokrito(pravokotniki,sirina,visina):
    # Če se nekja prekriva ali nekaj se nesme ponavljati uporabi MNOŽICO
    pokrite_koordinate = set()
    for x1,y1,x2,y2 in pravokotniki:
        pokrite_koordinate |= {(x,y) for x in range(x1,x2) for y in range(y1,y2)}
        # Lahko uporabimo zanko za zanko za vsako spremenljivko posebaj tako kot v zgornjem priimeru
    return sirina*visina - len(pokrite_koordinate)


def odstrani_zgresene(streli, pravokotniki):
    # Nesmes odstranjevati lemenetvo skozi katerega iteriraš s for zanko!
    i = 0
    while i < len(streli):
        x,y = streli[i]
        # any vrne boolena vrednost ce je ena stvar true je izraz true
        if any(x1 <= x <= x2 and y1 <= y <= y2 for x1,y1,x2,y2 in pravokotniki):
            i += 1
        else:
            del streli[i]


def je_zlata(stevilka, barve, pravokotniki):
    if pravokotniki[stevilka] == () and barve[stevilka] == "zlata":
        return True
    else:
        for pravokotnik in pravokotniki[stevilka]:
            if je_zlata(pravokotnik, barve, pravokotniki):
                return True
    return False


class Pravokotnik:

    def __init__(self, x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.streli = defaultdict(list)

    def strel(self, x, y, ime_strelca):
        self.streli[ime_strelca].append((x,y))

    def vseh_zadetkov(self):
        st_zadetkov = 0
        for s in self.streli.values():
            for strel in s:
                if self.x1 <= strel[0] <= self.x2 and self.y1 <= strel[1] <= self.y2:
                    st_zadetkov += 1
        return st_zadetkov

    def vseh_strelcev(self):
        return len([strelec for strelec in self.streli])

    def zadetkov(self, ime_strelca):
        st_zadetkov = 0
        for strel in self.streli[ime_strelca]:
            if self.x1 <= strel[0] <= self.x2 and self.y1 <= strel[1] <= self.y2:
                st_zadetkov += 1
        return st_zadetkov


class Test(unittest.TestCase):
    pravokotniki = [(0, 1, 4, 3),
                    (0, 6, 1, 8),
                    (2, 2, 7, 6),
                    (3, 4, 6, 5),
                    (5, 1, 9, 7),
                    (8, 0, 10, 2),
                    (8, 3, 10, 5),
                    (8, 6, 11, 8)]

    def test_01_preberi_pravokotnike(self):
        self.assertEqual(preberi_pravokotnike("pravokotniki.txt"), self.pravokotniki)

    def test_02_nepokritih(self):
        self.assertEqual(nepokrito(self.pravokotniki, 11, 8), 34)

    def test_03_odstrani_zgresene(self):
        streli = [(0.55, 0.4), (0.1, 5), (5.1, 3.2), (7.1, 7.1), (8.5, 3.5)]
        self.assertIsNone(odstrani_zgresene(streli, self.pravokotniki))
        self.assertEqual(streli, [(5.1, 3.2), (8.5, 3.5)])

    def test_04_je_zlata(self):
        prekritja = {3: (4, 5), 5: (1, ), 4: (6, 7, 8), 2: (), 1: (), 6: (), 7: (), 8: ()}
        barve = {1: "zlata", 2: "zlata", 3: "modra", 4: "rdeca", 5: "rumena",
                 6: "zelena", 7: "rumena", 8: "modra", 9: "zelena"}

        self.assertTrue(je_zlata(1, barve, prekritja))
        self.assertTrue(je_zlata(2, barve, prekritja))
        self.assertTrue(je_zlata(3, barve, prekritja))
        self.assertFalse(je_zlata(4, barve, prekritja))
        self.assertTrue(je_zlata(5, barve, prekritja))
        self.assertFalse(je_zlata(6, barve, prekritja))
        self.assertFalse(je_zlata(7, barve, prekritja))
        self.assertFalse(je_zlata(8, barve, prekritja))

        prekritja[3] = (5, 4)
        self.assertTrue(je_zlata(3, barve, prekritja))

        barve[8] = "zlata"
        barve[3] = "rumena"
        self.assertTrue(je_zlata(3, barve, prekritja))

        barve[8] = "modra"
        barve[6] = "zlata"
        self.assertTrue(je_zlata(3, barve, prekritja))

    def test_05_pravokotnik(self):
        pravokotnik = Pravokotnik(3, 2, 7, 6)
        self.assertEqual(pravokotnik.vseh_zadetkov(), 0)
        self.assertEqual(pravokotnik.vseh_strelcev(), 0)

        pravokotnik.strel(1, 1, "Ana")
        pravokotnik.strel(1, 2, "Ana")
        pravokotnik.strel(3.5, 1.5, "Ana")
        pravokotnik.strel(3.5, 7, "Ana")
        self.assertEqual(pravokotnik.vseh_zadetkov(), 0)
        self.assertEqual(pravokotnik.vseh_strelcev(), 1)
        self.assertEqual(pravokotnik.zadetkov("Ana"), 0)

        pravokotnik.strel(3.5, 4, "Ana")
        pravokotnik.strel(3.5, 4, "Ana")
        pravokotnik.strel(3.5, 4, "Berta")
        self.assertEqual(pravokotnik.vseh_zadetkov(), 3)
        self.assertEqual(pravokotnik.vseh_strelcev(), 2)
        self.assertEqual(pravokotnik.zadetkov("Ana"), 2)


if __name__ == "__main__":
    unittest.main()
