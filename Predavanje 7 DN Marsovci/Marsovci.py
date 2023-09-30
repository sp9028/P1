import math
from math import *

krogi = [
    (164.4, 136.8, 50.8),
    (59.2, 182.8, 50.8),
    (282.8, 71.5, 45.6),
    (391, 229.4, 58.4),
    (259.9, 186, 47.6),
    (428, 89, 63.2),
    (88.6, 44.3, 37.5),
    (371.6, 233.6, 10.6),
    (408.7, 210.5, 8.9),
    (398.1, 95.5, 13),
    (449.5, 99.6, 13.6),
    (455.4, 66.5, 12.4),
    (139.6, 138, 10.6),
    (185, 138, 10.6),
    (69.8, 46.5, 10.6),
    (267.4, 51.7, 17.2),
    (225.8, 187.3, 7.5),
    (242.8, 187.3, 7.5),
    (259.8, 187.3, 7.5),
    (276.7, 187.3, 7.5),
    (293.7, 187.3, 7.5),
    (267.4, 51.7, 10.6),
    (99.6, 43.1, 17.2),
    (99.6, 43.1, 10.6),
    (150.3, 245.5, 50.8),
    (144.3, 243.6, 38.8),
    (127.3, 245.5, 7.5),
    (161.3, 245.5, 7.5)]

from math import *


def ptici_priprava(krogi):
    notranji_krogi = set()
    vsi_krogi = set(krogi)

    for x,y,r in krogi:
        for x1,y1,r1 in krogi:
            if r > r1:
                if math.sqrt(math.pow(x-x1, 2) + math.pow(y-y1, 2)) < r:
                    notranji_krogi.add((x1, y1, r1))
    zunanji_krogi = vsi_krogi - notranji_krogi

    return zunanji_krogi


def ptici_priprava1(krogi):
    vsebovanost = {}

    for x,y,r in krogi:
        for x1,y1,r1 in krogi:
            if r > r1:
                if math.sqrt(math.pow(x-x1, 2) + math.pow(y-y1, 2)) < r:
                    vsebovanost.setdefault((x,y,r), []).append((x1,y1,r1))

    return vsebovanost


def ptici(krogi):
    zunanji_krogi = ptici_priprava(krogi)
    vsebovanost = ptici_priprava1(krogi)
    neptici = set()
    ptici = set()

    for x,y,r in krogi:
        if (x,y,r) in zunanji_krogi:
            kljuc = (x,y,r)
            if vsebovanost.get(kljuc) is None:
                neptici.add((x,y))
            elif len(vsebovanost.get(kljuc)) == 2:
                seznam = vsebovanost.get(kljuc)
                i = 0
                while i < len(seznam):
                    if seznam[i] in vsebovanost.keys():
                        neptici.add((x,y))
                    elif seznam[i] not in vsebovanost.keys():
                        ptici.add((x,y))
                    i += 1
    vsi_ptici = ptici - neptici
    return vsi_ptici


def letala(krogi):
    zunanji_krogi = ptici_priprava(krogi)
    vsebovanost = ptici_priprava1(krogi)
    neletala = set()
    letala = set()

    for x, y, r in krogi:
        if (x, y, r) in zunanji_krogi:
            kljuc = (x, y, r)
            if vsebovanost.get(kljuc) is None:
                neletala.add((x, y))
            elif len(vsebovanost.get(kljuc)) != 2:
                seznam = vsebovanost.get(kljuc)
                i = 0
                while i < len(seznam):
                    if seznam[i] in vsebovanost.keys():
                        neletala.add((x, y))
                    elif seznam[i] not in vsebovanost.keys():
                        letala.add((x, y))
                    i += 1
    vsa_letala = letala - neletala
    return vsa_letala


def sumljivi(krogi):
    vesoljci = ptici_priprava(krogi)
    vesoljci1 = set()
    vsi_ptici = ptici(krogi)
    vsa_letala = letala(krogi)

    for x,y,r in vesoljci:
        vesoljci1.add((x,y))

    unija = vsa_letala | vsi_ptici
    vsi_vesoljci = vesoljci1 - unija
    return vsi_vesoljci




import time
import unittest


class TestObvezna(unittest.TestCase):
    def setUp(self):
        self.zacetek = time.time()

    def tearDown(self):
        self.assertLess(time.time() - self.zacetek, 15,
                        "vsak test se mora končati hitreje kot v 15 sekundah")

    def test_ptici(self):
        self.assertEqual({(164.4, 136.8), (391, 229.4)}, ptici(krogi))

        self.assertEqual(set(), ptici([(x, x, 0.5) for x in range(1000)]))

        self.assertEqual(set(), ptici([(0, 0, x) for x in range(1000)]))

        self.assertEqual(set(), ptici([(x, x, r)
                                       for x in range(30 * 100, 100)
                                       for r in range(30)]))

        self.assertEqual({(-100, -100)},
                         ptici([(-100, -100, 10),
                                (-102, -100, 1),
                                (-99, -100, 1)] +
                               [(x, x, r)
                                for x in range(30 * 100, 100)
                                for r in range(50)]))

    def test_letala(self):
        self.assertEqual({(259.9, 186), (428, 89)}, letala(krogi))

        self.assertEqual(set(), letala([(x, x, 0.5) for x in range(1000)]))
        self.assertEqual(set(), letala([(0, 0, x) for x in range(1000)]))

        self.assertEqual(set(), letala([(x, x, r)
                                        for x in range(30 * 100, 100)
                                        for r in range(30)]))

        self.assertEqual({(0, 0), (100000, 0),},
                         letala([(0, 0, 10000),
                                 (100000, 0, 1), (100000, 0, 0.5),
                                 (200000, 0, 1)]
                                + [(x, 0, 0.5) for x in range(1000)]))

        self.assertEqual({(100000, 0)},
                         letala([(0, 0, 10000),
                                 (100000, 0, 1), (100000, 0, 0.5),
                                 (200000, 0, 1)]
                                + [(x, 0, 0.5) for x in range(500)]
                                + [(x, 0, 0.3) for x in range(500)]))


class TestDodatna(unittest.TestCase):
    def setUp(self):
        self.zacetek = time.time()

    def tearDown(self):
        self.assertLess(time.time() - self.zacetek, 15,
                        "vsak test se mora končati hitreje kot v 15 sekundah")

    def test_sumljivi(self):
        self.assertEqual({(59.2, 182.8),
                          (88.6, 44.3),
                          (150.3, 245.5),
                          (282.8, 71.5)},
                         sumljivi(krogi))

        crta = [(x, x, 0.5) for x in range(1000)]
        self.assertEqual({(x, y) for x, y, _ in crta}, sumljivi(crta))


        self.assertEqual({(0, 0)}, sumljivi([(0, 0, x) for x in range(1000)]))

        crta = {(x, x, 29) for x in range(30 * 100, 100)}
        self.assertEqual(crta,
                         sumljivi([(x, x, r)
                                   for x in range(30 * 100, 100)
                                   for r in range(30)]))

        self.assertEqual(crta,
                         sumljivi([(-100, -100, 10),
                                   (-102, -100, 1),
                                   (-99, -100, 1)] +
                                  [(x, x, r)
                                   for x in range(30 * 100, 100)
                                   for r in range(50)]))

        self.assertEqual({(200000, 0),},
                         sumljivi([(0, 0, 10000),
                                   (100000, 0, 1), (100000, 0, 0.5),
                                   (200000, 0, 1)]
                                  + [(x, 0, 0.5) for x in range(1000)]))

        self.assertEqual({(0, 0), (200000, 0)},
                         sumljivi([(0, 0, 10000),
                                   (100000, 0, 1), (100000, 0, 0.5),
                                   (200000, 0, 1)]
                                  + [(x, 0, 0.5) for x in range(500)]
                                  + [(x, 0, 0.3) for x in range(500)]))


if __name__ == "__main__":
    unittest.main()







