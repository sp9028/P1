import unittest


def preziveli(postavitev):
    vsi = set()
    prezivel = ""
    for figura, polje in postavitev:
        for figura1, polje1 in postavitev:
            if polje == polje1:
                prezivel = figura1
        vsi.add(prezivel)
    return vsi


def prosta_polja(kraljice):
    prosta = 0
    vsa_polja = set()
    vsa_polja |= {(x, y) for x in range(1, 9) for y in range(1, 9)}
    for x, y in vsa_polja:
        # Pri all morajo biti vsi pohoji true da vrne true. True vrne tudi = 1 in False = 0
        prosta += all(kx != x and ky != y and abs(kx - x) != abs(ky - y) for kx, ky in kraljice)
    return prosta


def dostopnih_polj(koordinate, zasedena):
    kx, ky = koordinate
    vrstica = [x for x, y in zasedena if y == ky] + [0, 9]
    stolpec = [y for x, y in zasedena if x == kx] + [0, 9]

    return (min(x for x in vrstica if x > kx) - max(x for x in vrstica if x < kx) - 1
            + min(y for y in stolpec if y > ky) - max(y for y in stolpec if y < ky) - 1 - 1)


def sciti_kmeta(x1, y1, x2, y2, kmetje):
    # Znak \ uporabimo če hočemo da se upošteva tudi koda v movi vrstici
    return abs(x1 - x2) == 1 and y2 == y1 + 1 \
        or (x1 - 1, y1 - 1) in kmetje and sciti_kmeta(x1 - 1, y1 + 1, x2, y2, kmetje) \
        or (x1 + 1, y1 + 1) in kmetje and sciti_kmeta(x1 + 1, y1 + 1, x2, y2, kmetje)


class Top:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self._razdalja = 0

    def premik(self, smer, polj):
        self._razdalja += polj
        if smer == ">":
            self.x += polj
        elif smer == "<":
            self.x -= polj
        elif smer == "v":
            self.y -= polj
        else:
            self.y += polj

    def koordinate(self):
        return (self.x,self.y)

    def razdalja(self):
        return self._razdalja


class StarTop(Top):

    def __init__(self, x,y):
        super().__init__(x,y)
        self.zahteve = []

    def premik(self, smer, polj):
        if polj > 3:
            self.zahteve.append(polj)
        if len(self.zahteve) > 1:
            self.zahteve.clear()
            pass
        else:
            # Dedovanje metode če hočemo poklicati metodo iz starševskega razreda gapokličemo z super().metoda
            super().premik(smer,polj)


class Testi(unittest.TestCase):
    def test_01_preziveli(self):
        self.assertEqual(preziveli({}), set())
        self.assertEqual(preziveli(
            [("kmet1", "a2"), ("kmet2", "b2"), ("kmet3", "c2"),
             ("lovec1", "c1"), ("top1", "a1"), ("konj2", "b2"),
             ("kraljica", "d1"), ("lovec2", "b2"), ("top2", "c2")]),
            {"kmet1", "lovec1", "top1", "kraljica", "lovec2", "top2"}
        )

    def test_02_prosta_polja(self):
        self.assertEqual(prosta_polja([]), 64)
        self.assertEqual(prosta_polja([(1, 1)]), 64 - 1 - 7 - 7 - 7)
        self.assertEqual(prosta_polja([(1, 1), (3, 1)]), 64 - 1 - 7 - 7 - 7 - 6 - 5)
        self.assertEqual(prosta_polja([(1, 1), (1, 3)]), 64 - 1 - 7 - 7 - 7 - 6 - 5)
        self.assertEqual(prosta_polja([(1, 1), (3, 3)]), 64 - 1 - 7 - 7 - 7 - 6 - 6 - 1 - 1)
        self.assertEqual(prosta_polja([(1, 1), (3, 5)]), 64 - 1 - 7 - 7 - 7 - 1 - 5 - 5 - 4 - 3)
        self.assertEqual(prosta_polja([(1, 1), (3, 7)]), 64 - 1 - 7 - 7 - 7 - 1 - 5 - 4 - 1 - 5 - 2)
        self.assertEqual(prosta_polja([(1, 1), (8, 8)]), 36 - 6)

    def test_03_dostopnih_polj(self):
        self.assertEqual(dostopnih_polj((3, 5), []), 15)
        figure = [(1, 2), (3, 5), (4, 2), (5, 3), (6, 2), (7, 3),
                  (8, 4), (6, 7), (1, 5), (6, 8)]
        self.assertEqual(dostopnih_polj((6, 5), figure), 8)
        self.assertEqual(dostopnih_polj((2, 5), figure), 8)
        self.assertEqual(dostopnih_polj((5, 2), figure), 2)
        self.assertEqual(dostopnih_polj((3, 8), figure), 7)

    def test_04_sciti_kmeta(self):
        kmetje = [(1, 3), (3, 5), (5, 3), (6, 4), (4, 2), (4, 4), (7, 3), (8, 4)]
        self.assertTrue(sciti_kmeta(4, 2, 5, 3, kmetje))
        self.assertTrue(sciti_kmeta(5, 3, 6, 4, kmetje))
        self.assertTrue(sciti_kmeta(4, 2, 6, 4, kmetje))
        self.assertTrue(sciti_kmeta(4, 2, 3, 5, kmetje))
        self.assertTrue(sciti_kmeta(4, 2, 6, 4, kmetje))
        self.assertTrue(sciti_kmeta(5, 3, 3, 5, kmetje))
        self.assertTrue(sciti_kmeta(5, 3, 4, 4, kmetje))
        self.assertTrue(sciti_kmeta(5, 3, 6, 4, kmetje))
        self.assertTrue(sciti_kmeta(4, 4, 3, 5, kmetje))
        self.assertTrue(sciti_kmeta(7, 3, 6, 4, kmetje))
        self.assertTrue(sciti_kmeta(7, 3, 6, 4, kmetje))
        self.assertTrue(sciti_kmeta(7, 3, 8, 4, kmetje))

        self.assertFalse(sciti_kmeta(1, 3, 3, 5, kmetje))
        self.assertFalse(sciti_kmeta(3, 5, 1, 3, kmetje))
        self.assertFalse(sciti_kmeta(5, 3, 4, 2, kmetje))
        self.assertFalse(sciti_kmeta(5, 3, 6, 2, kmetje))
        self.assertFalse(sciti_kmeta(4, 2, 1, 3, kmetje))
        self.assertFalse(sciti_kmeta(1, 3, 4, 2, kmetje))
        self.assertFalse(sciti_kmeta(3, 3, 4, 2, kmetje))

    def test_05a_top(self):
        t = Top(5, 3)
        self.assertEqual(t.koordinate(), (5, 3))
        self.assertEqual(t.razdalja(), 0)
        t.premik("^", 3)
        self.assertEqual(t.koordinate(), (5, 6))
        t.premik(">", 1)
        self.assertEqual(t.koordinate(), (6, 6))
        t.premik("v", 4)
        self.assertEqual(t.koordinate(), (6, 2))
        t.premik("<", 5)
        self.assertEqual(t.koordinate(), (1, 2))
        self.assertEqual(t.razdalja(), 13)

    def test_05b_star_top(self):
        self.assertEqual(StarTop.__bases__, (Top,))
        t = StarTop(5, 3)
        self.assertEqual(t.koordinate(), (5, 3))
        self.assertEqual(t.razdalja(), 0)
        t.premik("^", 3)
        self.assertEqual(t.koordinate(), (5, 6))
        t.premik(">", 1)
        self.assertEqual(t.koordinate(), (6, 6))
        t.premik("v", 4)
        self.assertEqual(t.koordinate(), (6, 2))
        self.assertEqual(t.razdalja(), 8)
        t.premik("<", 5)
        self.assertEqual(t.koordinate(), (6, 2))
        self.assertEqual(t.razdalja(), 8)
        t.premik("<", 5)
        self.assertEqual(t.koordinate(), (1, 2))
        self.assertEqual(t.razdalja(), 13)


if __name__ == "__main__":
    unittest.main()
