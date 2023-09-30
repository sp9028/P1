def dolzina_poti(s, o):
    pari = dict(s)
    i = 0
    while o in pari:
        i += 1
        o = pari[o]
    return i


def alterniraj(s):
    n = []
    for e in s:
        if not n or e * n[-1] < 0:
            n.append(e)
    s[:] = n


# Če imamo seznam terk če seznam pretvorimo v slovar dobimo slovar katerega ključi so
# prvi elementi terk, vrednosti posameznega ključa pa njegov drug element v njegvi terki


class Mesto:

    def __init__(self, sirina, visina):
        self.sirina = sirina
        self.visina = visina
        self.hise = set()

    def postavi(self, x, y):
        self.hise.add((x, y))

    def porusi(self, x0, y0, x1, y1):
        odstrani = set()
        for hisa in self.hise:
            x, y = hisa
            if (x >= x0 and y >= y0) and (x <= x1 and y <= y1):
                odstrani.add(hisa)
        self.hise -= odstrani

    def zasedeno(self):
        return len(self.hise)

    def __len__(mesto):
        return mesto.zasedeno()

    # Metoda v razredu prejme svoj objekt svojo različico tega classa. Če odtsranimo self potem metoda lahko prejme
    # katerikoli objekt tega razreda in potem z njim operira naprej

    def prosto(self):
        return self.visina * self.sirina - len(self.hise)


import unittest


class Test01DolzinaPoti(unittest.TestCase):
    def test_dolzina_poti(self):
        import random
        from itertools import chain

        stevilke = list(range(1, 100001))
        random.shuffle(stevilke)

        kosi = stevilke[:50000], stevilke[50000:70000], stevilke[70000:]
        pari = list(chain(*(zip(p, p[1:]) for p in kosi)))
        random.shuffle(pari)
        self.assertEqual(dolzina_poti([(1, 2), (3, 4), (2, 3)], 1), 3)
        self.assertEqual(dolzina_poti([(1, 2), (2, 3), (3, 4)], 2), 2)
        self.assertEqual(dolzina_poti([(1, 2), (2, 3), (3, 4), (5, 6)], 1), 3)
        self.assertEqual(dolzina_poti([(1, 2), (2, 3), (3, 4), (5, 6)], 5), 1)
        self.assertEqual(dolzina_poti([(1, 2), (2, 3), (3, 4), (5, 6)], 6), 0)
        self.assertEqual(dolzina_poti(pari, stevilke[0]), 49999)
        self.assertEqual(dolzina_poti(pari, stevilke[1]), 49998)
        self.assertEqual(dolzina_poti(pari, stevilke[50000]), 19999)


class Test02Alterniraj(unittest.TestCase):
    def test_alterniraj(self):
        s = [3, 4, -1, 1, -5, -2, -1, 7, -8]
        self.assertIsNone(alterniraj(s))
        self.assertEqual(s, [3, -1, 1, -5, 7, -8])

        s = [3, 4, 8, 1, 2]
        self.assertIsNone(alterniraj(s))
        self.assertEqual(s, [3])

        s = [3, 4, 8, 1, -4, 2]
        self.assertIsNone(alterniraj(s))
        self.assertEqual(s, [3, -4, 2])

        s = []
        self.assertIsNone(alterniraj(s))
        self.assertEqual(s, [])

        s = [-1]
        self.assertIsNone(alterniraj(s))
        self.assertEqual(s, [-1])

        s = [5]
        self.assertIsNone(alterniraj(s))
        self.assertEqual(s, [5])


class Test03NimaVhoda(unittest.TestCase):
    def test_nima_vhoda(self):
        # https://ucilnica.fri.uni-lj.si/mod/assign/view.php?id=17726
        instr = {1: (('bot', 3), ('bot', 4)),
                 2: (('bot', 4), ('output', 0)),
                 3: (('output', 5), ('bot', 5)),
                 4: (('bot', 5), ('bot', 6)),
                 5: (('output', 1), ('bot', 7)),
                 6: (('bot', 7), ('output', 4)),
                 7: (('output', 2), ('output', 3))}
        self.assertEqual(nima_vhoda(instr), ({1, 2}, {3, 6}))


class Test04NaPoti(unittest.TestCase):
    def test_na_poti(self):
        instr = {1: (('bot', 3), ('bot', 4)),
                 2: (('bot', 4), ('output', 0)),
                 3: (('output', 5), ('bot', 5)),
                 4: (('bot', 5), ('bot', 6)),
                 5: (('output', 1), ('bot', 7)),
                 6: (('bot', 7), ('output', 4)),
                 7: (('output', 2), ('output', 3))}
        self.assertTrue(na_poti(1, 1, instr))
        self.assertFalse(na_poti(1, 2, instr))
        self.assertTrue(na_poti(1, 3, instr))
        self.assertTrue(na_poti(1, 4, instr))
        self.assertTrue(na_poti(1, 5, instr))
        self.assertTrue(na_poti(1, 6, instr))
        self.assertTrue(na_poti(1, 7, instr))

        self.assertFalse(na_poti(2, 1, instr))
        self.assertTrue(na_poti(2, 2, instr))
        self.assertFalse(na_poti(2, 3, instr))
        self.assertTrue(na_poti(2, 4, instr))
        self.assertTrue(na_poti(2, 5, instr))
        self.assertTrue(na_poti(2, 6, instr))
        self.assertTrue(na_poti(2, 7, instr))

        self.assertFalse(na_poti(4, 1, instr))
        self.assertFalse(na_poti(4, 2, instr))
        self.assertFalse(na_poti(4, 3, instr))
        self.assertTrue(na_poti(4, 4, instr))
        self.assertTrue(na_poti(4, 5, instr))
        self.assertTrue(na_poti(4, 6, instr))
        self.assertTrue(na_poti(4, 7, instr))

        self.assertFalse(na_poti(5, 1, instr))

        self.assertFalse(na_poti(7, 1, instr))
        self.assertFalse(na_poti(7, 2, instr))
        self.assertFalse(na_poti(7, 3, instr))
        self.assertFalse(na_poti(7, 4, instr))
        self.assertFalse(na_poti(7, 5, instr))
        self.assertFalse(na_poti(7, 6, instr))
        self.assertTrue(na_poti(7, 7, instr))


class Test05Mesto(unittest.TestCase):
    def test_mesto(self):
        m = Mesto(5, 8)
        self.assertEqual(len(m), 0)
        self.assertEqual(m.prosto(), 40)

        m.postavi(2, 6)
        self.assertEqual(len(m), 1)
        self.assertEqual(m.prosto(), 39)

        m.postavi(2, 6)
        self.assertEqual(len(m), 1)
        self.assertEqual(m.prosto(), 39)

        for x in range(4):
            for y in range(2, 5):
                m.postavi(x, y)
        self.assertEqual(len(m), 13)
        self.assertEqual(m.prosto(), 27)

        m.porusi(1, 1, 2, 4)
        self.assertEqual(len(m), 7)
        self.assertEqual(m.prosto(), 33)


if __name__ == "__main__":
    unittest.main()
