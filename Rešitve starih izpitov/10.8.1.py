import unittest
from collections import defaultdict

def preberi_strele(ime_datoteke):
    seznam = []
    for v in open(ime_datoteke):
        ime,koordinati = v.strip().split(":")
        x,y = koordinati.strip().split(",")
        seznam.append((ime,float(x),float(y)))
    return seznam


def najboljsi_strelec(streli, pravokotniki):
    strelci = {}
    enakodobri = set()
    for ime, sx1, sy1 in streli:
        if ime not in strelci:
            strelci[ime] = 0
        if any(x1 <= sx1 <= x2 and y1 <= sy1 <= y2 for x1,y1,x2,y2 in pravokotniki):
            strelci[ime] += 1

    for strelec1 in strelci:
        for strelec2 in strelci:
            if strelec1 != strelec2 and strelci[strelec2] == strelci[strelec1]:
                enakodobri |= {x for x in [strelec1,strelec2]}

    if len(enakodobri) > 1:
        return sorted(list(enakodobri))[0]
    else:
        return max(strelci, key=strelci.get)


def odstrani_zadete(x,y,pravokotniki):
    i = 0
    while i < len(pravokotniki):
        x1,y1,x2,y2 = pravokotniki[i]
        if x1 <= x <= x2 and y1 <= y <= y2:
            del pravokotniki[i]
        else:
            i += 1


def naj_levo(zacetek, pravokotniki, prekrivanja):
    levo = pravokotniki[zacetek][0]
    if prekrivanja[zacetek] == ():
        return levo
    else:
        for pravokotnik in prekrivanja[zacetek]:
            levo_spod = naj_levo(pravokotnik, pravokotniki, prekrivanja)
            if levo_spod < levo:
                levo = levo_spod
        return levo


class Turnir:

    def __init__(self, pravokotniki):
        self.pravokotniki = pravokotniki
        self.streli = []
        self.zadetki = {}

        for pravokotnik in pravokotniki:
            self.zadetki[pravokotnik] = 0

    def strel(self, x,y):
        for pravokotnik in self.zadetki:
            x1,y1,x2,y2 = pravokotnik
            if x1 <= x <= x2 and y1 <= y <= y2:
                self.zadetki[pravokotnik] += 1

    def zadetkov(self, x1,y1,x2,y2):
        return self.zadetki[(x1,y1,x2,y2)]


class Test(unittest.TestCase):
    pravokotniki = [(0, 1, 4, 3),
                    (0, 6, 1, 8),
                    (2, 2, 7, 6),
                    (3, 4, 6, 5),
                    (5, 1, 9, 7),
                    (8, 0, 10, 2),
                    (8, 3, 10, 5),
                    (8, 6, 11, 8)]

    def test_01_preberi_strele(self):
        self.assertEqual(
            preberi_strele("streli.txt"),
            [("Ana", 0.55, 3.14), ("Berta", 5.5, 4.5), ("Ana", 6.5, 6.5), ("Cilka", 10.3, 6.3)])

    def test_02_najboljsi_strelec(self):
        self.assertEqual(najboljsi_strelec(
            [("Ana", 1.5, 1.5), ("Berta", 4.4, 1.4), ("Berta", 6, 4), ("Ana", 9, 7)], self.pravokotniki),
            "Ana")
        self.assertEqual(najboljsi_strelec(
            [("Berta", 6, 4), ("Ana", 1.5, 1.5), ("Berta", 4.4, 1.4), ("Ana", 9, 7)], self.pravokotniki),
            "Ana")
        self.assertEqual(najboljsi_strelec(
            [("Ana", 1.5, 1.5), ("Berta", 4.4, 1.4), ("Berta", 6, 4), ("Ana", 9, 7), ("Berta", 9, 7)], self.pravokotniki),
            "Ana")
        self.assertEqual(najboljsi_strelec(
            [("Ana", 1.5, 1.5), ("Berta", 4.4, 1.4), ("Berta", 6, 4), ("Berta", 9, 7)], self.pravokotniki),
            "Berta")
        self.assertEqual(najboljsi_strelec(
            [("Ana", 1.5, 1.5), ("Berta", 4.4, 1.4), ("Berta", 6, 4), ("Berta", 9, 7), ("Ana", 9, 7)], self.pravokotniki),
            "Ana")

        self.assertEqual(najboljsi_strelec(
            [("Ana", 0, 0)], self.pravokotniki),
            "Ana")

    def test_03_odstrani_zadete(self):
        prav1 = self.pravokotniki[:]
        self.assertIsNone(odstrani_zadete(5.5, 4.5, prav1))
        self.assertEqual(prav1, self.pravokotniki[:2] + self.pravokotniki[5:])

        prav1 = self.pravokotniki[:]
        self.assertIsNone(odstrani_zadete(5.5, 5.5, prav1))
        self.assertEqual(prav1, self.pravokotniki[:2] + [self.pravokotniki[3]] + self.pravokotniki[5:])

        prav1 = self.pravokotniki[:]
        self.assertIsNone(odstrani_zadete(0, 0, prav1))
        self.assertEqual(prav1, self.pravokotniki)

        prav1 = self.pravokotniki[:]
        self.assertIsNone(odstrani_zadete(2.5, 2.5, prav1))
        self.assertEqual(prav1, self.pravokotniki[1:2] + self.pravokotniki[3:])

    def test_04_naj_levo(self):
        prekrivanja = {3: (2,), 2: (0, 4), 4: (5, 6, 7), 1: (), 0: (), 5: (),
                       6: (), 7: ()}
        pravokotniki = self.pravokotniki
        self.assertEqual(naj_levo(3, pravokotniki, prekrivanja), 0)
        self.assertEqual(naj_levo(4, pravokotniki, prekrivanja), 5)
        self.assertEqual(naj_levo(2, pravokotniki, prekrivanja), 0)
        self.assertEqual(naj_levo(0, pravokotniki, prekrivanja), 0)
        self.assertEqual(naj_levo(1, pravokotniki, prekrivanja), 0)
        self.assertEqual(naj_levo(5, pravokotniki, prekrivanja), 8)

        prekrivanja = {3: (2,), 2: (4, ), 4: (5, 6, 7), 1: (), 0: (2, ), 5: (),
                       6: (), 7: ()}
        self.assertEqual(naj_levo(3, pravokotniki, prekrivanja), 2)
        self.assertEqual(naj_levo(4, pravokotniki, prekrivanja), 5)
        self.assertEqual(naj_levo(2, pravokotniki, prekrivanja), 2)
        self.assertEqual(naj_levo(0, pravokotniki, prekrivanja), 0)
        self.assertEqual(naj_levo(1, pravokotniki, prekrivanja), 0)
        self.assertEqual(naj_levo(5, pravokotniki, prekrivanja), 8)

        prekrivanja = {3: (2,), 2: (4, ), 4: (6, 7), 1: (), 0: (2, ), 5: (4, ),
                       6: (), 7: ()}
        self.assertEqual(naj_levo(5, pravokotniki, prekrivanja), 5)

        prav1 = pravokotniki[:]
        prav1[0] = (2, 1, 4, 3)  # levi rob se premakne na 2
        prav1[2] = (1, 2, 6, 5)  # levi rob se premakne na 1
        prav1[3] = (3, 2, 6, 5)  # gornji rob gre na 2
        prekrivanja = {3: (0, 4), 4: (2, 6, 7), 2: (), 1: (), 0: (), 5: (4, ), 6: (), 7: ()}

        # črv mora iz 3 na 4 in potem na 2, ker se 0 ne dotika 2 (vmes je ... emm zrak)
        self.assertEqual(naj_levo(3, prav1, prekrivanja), 1)

        # 5 -> 4 -> 2
        self.assertEqual(naj_levo(5, prav1, prekrivanja), 1)

        # ne more nikamor
        self.assertEqual(naj_levo(6, prav1, prekrivanja), 8)

    def test_05_turnir(self):
        turnir = Turnir(self.pravokotniki)
        turnir.strel(2.5, 2.5)
        turnir.strel(1.5, 2.5)
        turnir.strel(5.5, 4.1)
        self.assertEqual(turnir.zadetkov(0, 1, 4, 3), 2)
        self.assertEqual(turnir.zadetkov(0, 6, 1, 8), 0)
        self.assertEqual(turnir.zadetkov(2, 2, 7, 6), 2)
        self.assertEqual(turnir.zadetkov(3, 4, 6, 5), 1)


if __name__ == "__main__":
    unittest.main()
