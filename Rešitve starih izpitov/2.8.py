#Izpit 2015/16 29.januar


from collections import defaultdict


def cokolada(n, odlomi):
    vsi_koscki = n*n
    s = n
    v = n
    for lomljenje in odlomi:
        lomljenje1 = lomljenje.replace("", " ").strip()
        lomljenje2 = lomljenje1.split(" ")
        if len(lomljenje2) > 2:
            st = int("".join(lomljenje2[1:]))
        else:
            st = int(lomljenje2[1])
        if st <= n and (lomljenje2[0] == '<' or lomljenje2[0] == '>'):
            v -= st
        elif st > n and (lomljenje2[0] == '<' or lomljenje2[0] == '>'):
            v -= st
        elif st <= n and (lomljenje2[0] == 'v' or lomljenje2[0] == '^'):
            s -= st
        elif st > n and (lomljenje2[0] == 'v' or lomljenje2[0] == '^'):
            s -= st
    if s < 0 or v < 0:
        return 0
    return s * v


def zdruzi(s):
    slovar = defaultdict(set)
    for i,st in enumerate(s):
        slovar[st].add(i)
    return slovar

def razmeci(s):
    seznam = []
    m = set()
    for mnozica in s.values():
        for index in mnozica:
            m.add(index)
    for index in m:
        for st in s:
            if index in s[st]:
                seznam.append(st)
    return seznam


def brez_jecljanja_rec(s):
    if len(s) < 2:
        return s
    if s[0] == s[1]:
        return brez_jecljanja_rec(s[1:])
    else:
        return [s[0]] + brez_jecljanja_rec(s[1:])


def sopomena(stavek1, stavek2, sopomenke):
    stavek1,stavek2 = stavek1.split(), stavek2.split()
    if len(stavek1) != len(stavek2):
        return False
    for beseda1, beseda2 in zip(stavek1,stavek2):
        if beseda1 != beseda2:
            for so in sopomenke:
                if beseda1 in so and beseda2 in so:
                    break
            else:
                return False
    return True



class Picerija:

    kup = ["margerita", "klasika", "zelenjavna","siri"]

    # Skozi zip() lahko iteriramo samo enkrat

    def __init__(self):
        self.vse_pice = []
        self._zasluzek = 0

    def speci(self):
        self.vse_pice += self.kup

    def prodaj(self):
        cene = zip(self.kup,[1,2,1,3])
        if self.vse_pice:
            pica = self.vse_pice.pop()
            for pizza,cena in cene:
                if pica == pizza:
                    self._zasluzek += cena
            return pica

    def zasluzek(self):
        return self._zasluzek

    def __len__(self):
        return len(self.vse_pice)

    def __getitem__(self, item):
        return self.vse_pice[-item]

    def __str__(self):
        return " > ".join(self.vse_pice)

import unittest
class Naloga_1_Cokolada(unittest.TestCase):
    def test_cokolada(self):
        self.assertEqual(cokolada(10, ["<2", ">1", "^3", "^1", "v2", "<1"]), 24)
        self.assertEqual(cokolada(100, ["<20", ">13", "^3", "^18", "v12", "<1"]), 4422)
        self.assertEqual(cokolada(10, ["<2", ">8", "^3", "^1", "v2", "<1"]), 0)
        self.assertEqual(cokolada(10, ["<2"]), 80)
        self.assertEqual(cokolada(10, ["<12"]), 0)
        self.assertEqual(cokolada(6, []), 36)


class Naloga_2_ZdruziRazmeci(unittest.TestCase):
    def test_zdruzi(self):
        self.assertEqual(zdruzi([5, 1, 2, 5, 1, 8]), {5: {0, 3}, 1: {1, 4}, 2: {2}, 8: {5}})
        self.assertEqual(zdruzi([5, 1]), {5: {0}, 1: {1}})
        self.assertEqual(zdruzi([]), {})

    def test_razmeci(self):
        self.assertEqual(razmeci({5: {0, 3}, 1: {1, 4}, 2: {2}, 8: {5}}), [5, 1, 2, 5, 1, 8])
        self.assertEqual(razmeci({1: {2}, 0: {1, 3, 5}, 42: {0, 4}}), [42, 0, 1, 0, 42, 0])


class Naloga_3_BrezJecljanja(unittest.TestCase):
    def test_brez_jecljanja_rec(self):
        with self.assertRaises(RecursionError,
                               msg="Funkcija mora biti rekurzivna"):
            brez_jecljanja_rec(list(range(2000)))
            brez_jecljanja_rec([0] * 2000)

        self.assertEqual(brez_jecljanja_rec([1, 1, 2, 3, 4, 1, 1, 1]), [1, 2, 3, 4, 1])
        self.assertEqual(brez_jecljanja_rec([8, 4, 7, 9, 4, 6]), [8, 4, 7, 9, 4, 6])
        self.assertEqual(brez_jecljanja_rec([42]), [42])
        self.assertEqual(brez_jecljanja_rec([42, 42, 42]), [42])
        self.assertEqual(brez_jecljanja_rec([]), [])
        self.assertEqual(brez_jecljanja_rec([1, 2, 3, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(brez_jecljanja_rec([1, 2, 4, 3, 3, 5]), [1, 2, 4, 3, 5])
        self.assertEqual(brez_jecljanja_rec([1, 2, 4, 5, 3, 3]), [1, 2, 4, 5, 3])
        self.assertEqual(brez_jecljanja_rec([3, 3, 1, 2, 4, 5]), [3, 1, 2, 4, 5])
        self.assertEqual(brez_jecljanja_rec([3, 3, 1, 2, 3, 3, 4, 5, 3, 3]), [3, 1, 2, 3, 4, 5, 3])
        self.assertEqual(brez_jecljanja_rec([3, 3, 1, 2, 3, 4, 5, 3, 3]), [3, 1, 2, 3, 4, 5, 3])
        self.assertEqual(brez_jecljanja_rec([3, 3, 1, 2, 3, 4, 5, 3]), [3, 1, 2, 3, 4, 5, 3])
        self.assertEqual(brez_jecljanja_rec([3, 1, 2, 3, 4, 5, 3, 3]), [3, 1, 2, 3, 4, 5, 3])

        self.assertEqual(brez_jecljanja_rec(list("ABCAACCBA")), list("ABCACBA"))


    def test_brez_jecljanja_gen(self):
        self.assertEqual(brez_jecljanja_gen([1, 1, 2, 3, 4, 1, 1, 1]), [1, 2, 3, 4, 1])
        self.assertEqual(brez_jecljanja_gen([8, 4, 7, 9, 4, 6]), [8, 4, 7, 9, 4, 6])
        self.assertEqual(brez_jecljanja_gen([42]), [42])
        self.assertEqual(brez_jecljanja_gen([42, 42, 42]), [42])
        self.assertEqual(brez_jecljanja_gen([]), [])
        self.assertEqual(brez_jecljanja_gen([1, 2, 3, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(brez_jecljanja_gen([1, 2, 4, 3, 3, 5]), [1, 2, 4, 3, 5])
        self.assertEqual(brez_jecljanja_gen([1, 2, 4, 5, 3, 3]), [1, 2, 4, 5, 3])
        self.assertEqual(brez_jecljanja_gen([3, 3, 1, 2, 4, 5]), [3, 1, 2, 4, 5])
        self.assertEqual(brez_jecljanja_gen([3, 3, 1, 2, 3, 3, 4, 5, 3, 3]), [3, 1, 2, 3, 4, 5, 3])
        self.assertEqual(brez_jecljanja_gen([3, 3, 1, 2, 3, 4, 5, 3, 3]), [3, 1, 2, 3, 4, 5, 3])
        self.assertEqual(brez_jecljanja_gen([3, 3, 1, 2, 3, 4, 5, 3]), [3, 1, 2, 3, 4, 5, 3])
        self.assertEqual(brez_jecljanja_gen([3, 1, 2, 3, 4, 5, 3, 3]), [3, 1, 2, 3, 4, 5, 3])

        self.assertEqual(brez_jecljanja_gen(list("ABCAACCBA")), list("ABCACBA"))


class Naloga_4_Sopomenke(unittest.TestCase):
    def test_sopomena(self):
        sinonimi = [{"fant", "deček", "pob"},
                    {"dekle", "punca"},
                    {"cesta", "pot", "kolovoz", "makadam"},
                    {"kis", "jesih"},
                    {"noge", "tace"}]
        self.assertTrue(
            sopomena("pob in dekle sta vzela pot pod noge",
                     "pob in dekle sta vzela pot pod noge", sinonimi))
        self.assertTrue(
            sopomena("pob in dekle sta vzela pot pod noge",
                     "fant in punca sta vzela pot pod tace", sinonimi))
        self.assertTrue(
            sopomena("pob in dekle sta vzela kolovoz pod noge",
                     "fant in punca sta vzela pot pod tace", sinonimi))
        self.assertTrue(
            sopomena("fant in punca sta vzela pot pod tace",
                     "pob in dekle sta vzela pot pod noge", sinonimi))
        self.assertTrue(
            sopomena("fant in punca sta vzela pot pod tace",
                     "pob in dekle sta vzela kolovoz pod noge", sinonimi))

        self.assertFalse(
            sopomena("pob in dekle sta vzela pot pod noge",
                     "fant in deček sta vzela pot pod tace", sinonimi))
        self.assertFalse(
            sopomena("pob in dekle sta vzela pot pod noge",
                     "fant in deček sta vzela pot pod tace", sinonimi))

        self.assertFalse(
            sopomena("pob in dekle sta vzela pot pod noge",
                     "fant in punca sta vzela pot pod tace",
                     [{"fant", "deček", "pob"}]))


class Naloga_5_Picerija(unittest.TestCase):
    def setUp(self):
        self.pizze = "margerita > klasika > zelenjavna > siri"

    def test_1_init_len(self):
        p = Picerija()
        self.assertEqual(len(p), 0)

    def test_2_speci_str(self):
        p = Picerija()
        q = Picerija()
        p.speci()
        self.assertEqual(len(p), 4)
        self.assertEqual(str(p), self.pizze)
        p.speci()
        self.assertEqual(len(p), 8)
        self.assertEqual(str(p), self.pizze + " > " + self.pizze)
        self.assertEqual(len(q), 0)

        r = Picerija()
        self.assertEqual(len(p), 8)
        self.assertEqual(len(q), 0)
        self.assertEqual(len(r), 0)

        q.speci()
        self.assertEqual(len(p), 8)
        self.assertEqual(len(q), 4)
        self.assertEqual(len(r), 0)

    def test_3_prodaj_zasluzek(self):
        p = Picerija()
        q = Picerija()
        p.speci()
        q.speci()
        q.speci()
        self.assertEqual(p.prodaj(), "siri")
        self.assertEqual(p.prodaj(), "zelenjavna")
        self.assertEqual(q.prodaj(), "siri")
        self.assertEqual(p.prodaj(), "klasika")
        self.assertEqual(p.prodaj(), "margerita")
        self.assertIsNone(p.prodaj())
        self.assertEqual(q.prodaj(), "zelenjavna")
        self.assertIsNone(p.prodaj())

        self.assertEqual(p.zasluzek(), 7)
        self.assertEqual(q.zasluzek(), 4)

        q.speci()
        self.assertEqual(q.prodaj(), "siri")
        self.assertEqual(q.prodaj(), "zelenjavna")
        self.assertEqual(q.prodaj(), "klasika")
        self.assertEqual(q.prodaj(), "margerita")
        self.assertEqual(q.prodaj(), "klasika")
        self.assertEqual(q.prodaj(), "margerita")
        self.assertIsNone(p.prodaj())

    def test_4_get_item(self):
            p = Picerija()
            p.speci()
            p.speci()
            self.assertEqual(p[1], "siri")
            self.assertEqual(p[2], "zelenjavna")
            self.assertEqual(p[3], "klasika")
            self.assertEqual(p[4], "margerita")
            p.prodaj()
            self.assertEqual(p[1], "zelenjavna")
            self.assertEqual(p[2], "klasika")
            self.assertEqual(p[3], "margerita")
            self.assertEqual(p[4], "siri")
            self.assertEqual(p[5], "zelenjavna")
            self.assertEqual(p[6], "klasika")
            self.assertEqual(p[7], "margerita")


if __name__ == "__main__":
    unittest.main()
