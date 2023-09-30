import math
import unittest
from collections import defaultdict

def preblizu(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2) < 1.5


def koordinate(ime, osebe):
    for _ime,x,y in osebe:
        if _ime == ime:
            return (x,y)


def krsitelji(osebe):
    vsi_krsitelji = set()
    for ime1,x1,y1 in osebe:
        for ime2,x2,y2 in osebe:
            if preblizu(x1,y1,x2,y2) and ime1 != ime2:
                vsi_krsitelji |= {ime1,ime2}
    return vsi_krsitelji


def kazni(osebe):
    vse_kazni = defaultdict(int)
    for ime1,x1,y1 in osebe:
        for ime2,x2,y2 in osebe:
            if preblizu(x1,y1,x2,y2) and ime1 != ime2:
                vse_kazni[ime1] += 1
    return vse_kazni


def okuzeni(ime, osebe):
    vsi = {ime}
    x1,y1 = koordinate(ime, osebe)
    for ime2,x2,y2 in osebe:
        if preblizu(x1, y1, x2, y2) and ime != ime2 and y2 < y1:
            vsi |= okuzeni(ime2, osebe)
    return vsi


def kihanje(imena, osebe):
    odstranjeni = set()
    for ime in imena:
        if ime not in odstranjeni:
            odstranjeni |= {ime}
            x1,y1 = koordinate(ime, osebe)
            for ime1,x2,y2 in osebe:
                if ime != ime1 and preblizu(x1, y1, x2, y2):
                    odstranjeni |= {ime1}
    return {oseba for oseba,_,_ in osebe} - odstranjeni


class Prireditev:

    def __init__(self, min_razdalja):
        self.min_razdalja = min_razdalja
        self.osebe = set()

    def prihod(self, ime,x,y):
        if not self.osebe:
            self.osebe.add((ime,x,y))
        else:
            for oseba,x1,y1 in self.osebe:
                if math.sqrt((x-x1)**2 + (y-y1)**2) < self.min_razdalja:
                    break
            else:
                self.osebe.add((ime,x,y))

    def udelezenci(self):
        return {ime for ime,_,_ in self.osebe}



class Test(unittest.TestCase):
    osebe = [("Ana", 2, 4.5),
             ("Berta", 1, 3),
             ("Cilka", 1, 4),
             ("Dani", -1, 2),
             ("Ema", 1, 1),
             ("Fanči", 2, 0.5),
             ("Greta", -1, -1.5),
             ("Helga", 0, -1),
             ("Iva", 2, 0),
             ("Jana", 0, 0),
             ("Klara", 5, 1)
             ]

    def test_0_preblizu(self):
        self.assertTrue(preblizu(5, 3, 6, 2))
        self.assertTrue(preblizu(5, 2, 5, 2))
        self.assertTrue(preblizu(6, 2, 5, 3))
        self.assertTrue(preblizu(0, 0, 1.4, 0))
        self.assertFalse(preblizu(5, 3, 6, 1))

    def test_0_koordinate(self):
        self.assertEqual((-1, 2), koordinate("Dani", self.osebe))

    def test_1_krsitelji(self):
        self.assertEqual(
            set("Ana Berta Cilka Ema Fanči Greta Helga Iva Jana".split()),
            krsitelji(self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Ema Fanči Greta Helga Iva Jana".split()),
            krsitelji(self.osebe[:-1])
        )
        self.assertEqual(
            set("Greta Helga Jana".split()),
            krsitelji(self.osebe[-5:])
        )
        self.assertEqual(
            set(),
            krsitelji(self.osebe[:2])
        )

    def test_2_kazni(self):
        self.assertEqual(
            {"Ana": 1, "Berta": 1, "Cilka": 2, "Ema": 3,
             "Fanči": 2, "Greta": 1, "Helga": 2, "Iva": 2, "Jana": 2},
            kazni(self.osebe)
        )

    def test_3_okuzenih(self):
        self.assertEqual(
            {"Ema", "Fanči", "Iva", "Jana", "Greta", "Helga"},
            okuzeni("Ema", self.osebe))
        self.assertEqual(
            {"Jana", "Greta", "Helga"},
            okuzeni("Jana", self.osebe))
        self.assertEqual(
            {"Ana", "Berta", "Cilka"},
            okuzeni("Ana", self.osebe))
        self.assertEqual(
            {"Berta"},
            okuzeni("Berta", self.osebe))
        self.assertEqual(
            {"Klara"},
            okuzeni("Klara", self.osebe))

    def test_4_kihanje(self):
        self.assertEqual(
            set("Ana Berta Cilka Dani Ema Fanči Greta Helga Iva Jana Klara".split()),
            kihanje([], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Greta Helga Jana Klara".split()),
            kihanje(["Fanči"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Greta Helga Klara".split()),
            kihanje(["Ema"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Greta Helga Klara".split()),
            kihanje(["Ema", "Jana"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Greta Helga Klara".split()),
            kihanje(["Ema", "Fanči"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Greta Helga".split()),
            kihanje(["Ema", "Fanči", "Klara"], self.osebe)
        )
        self.assertEqual(
            set("Dani Greta Helga".split()),
            kihanje(["Ema", "Fanči", "Klara", "Cilka"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Fanči Greta Iva Klara".split()),
            kihanje(["Jana", "Helga", "Ema"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Klara".split()),
            kihanje(["Helga", "Ema", "Jana"], self.osebe)
        )

    def test_5_prireditev(self):
        g = Prireditev(1.5)
        for ime, x, y in self.osebe:
            g.prihod(ime, x, y)
        self.assertEqual(
            {"Ana", "Berta", "Dani", "Ema", "Greta", "Klara"},
            g.udelezenci()
        )

        g = Prireditev(1.5)
        for ime, x, y in self.osebe:
            if ime != "Ema":
                g.prihod(ime, x, y)
        self.assertEqual(
            {"Ana", "Berta", "Dani", "Fanči", "Greta", "Jana", "Klara"},
            g.udelezenci()
        )

        g = Prireditev(3)
        for ime, x, y in self.osebe:
            g.prihod(ime, x, y)
        self.assertEqual(
            {"Ana", "Dani", "Fanči", "Greta", "Klara"},
            g.udelezenci()
        )


if __name__ == "__main__":
    unittest.main()

