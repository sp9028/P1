# Izpit 2015/16 29.januar

import random
from collections import defaultdict

def ne_na_lihih(s):
    mnozica = set()
    preveri = True
    index = 0
    for st in s:
        if index % 2 == 0:
            index2 = 0
            for st2 in s:
                if st2 == st and index2 % 2 != 0:
                    preveri = False
                    break
                elif st2 == st and index2 % 2 == 0:
                    preveri = True
                index2 += 1
            if preveri:
                mnozica.add(st)
        index += 1
    return mnozica

#x[startAt:endBefore:skip]

def intervali(s):
    sez = []
    zac = 0
    while zac < len(s):
        konc = zac + 1
        while konc < len(s) and s[konc] == s[konc - 1] + 1:
            konc += 1
        sez.append((s[zac], s[konc - 1]))
        zac = konc
    return sez


def indeksi_rec(s,e):
    sez = []
    if not s:
        return []
    if s[-1] == e:
        return indeksi_rec(s[:-1],e) + [len(s) - 1]
    else:
        return indeksi_rec(s[:-1],e)


def predelaj(stavek1,sopomenke):
    sopomenke1 = {}
    for beseda in stavek1.split(" "):
        for skupina in sopomenke:
            if beseda in skupina:
                sopomenke1[beseda] = list(skupina - {beseda})

    nov_stavek = []
    for beseda in stavek1.split():
        if beseda in sopomenke1:
            nov_stavek.append(random.choice(sopomenke1[beseda]))
        else:
            nov_stavek.append(beseda)
    return " ".join(nov_stavek)


class PicerijaNaZalogo:
    zasluzki = {"margerita": 1, "klasika": 2, "zelenjavna": 1, "siri": 3}

    def __init__(self):
        self.zaloga = defaultdict(int)
        self.zasluzek1 = 0

    def speci(self, vrsta):
        self.zaloga[vrsta] += 1

    def prodaj(self, vrsta):
        if self.zaloga[vrsta]:
            self.zaloga[vrsta] -= 1
            self.zasluzek1 += self.zasluzki[vrsta]

    def zasluzek(self):
        return self.zasluzek1

    def __str__(self):
        return ", ".join(sorted(set(v for v, k in self.zaloga.items() if k)))

    def __len__(self):
        return sum(self.zaloga.values())



import unittest
class Naloga_1_NeNaLihih(unittest.TestCase):
    def test_ne_na_lihih(self):
        self.assertEqual(ne_na_lihih([0, 1, 2, 3, 4]), {0, 2, 4})
        self.assertEqual(ne_na_lihih([0, 1, 2, 3, 4, 2]), {0, 4})
        self.assertEqual(ne_na_lihih([0, 2, 2, 3, 4]), {0, 4})
        self.assertEqual(ne_na_lihih([1, 1, 1]), set())
        self.assertEqual(ne_na_lihih([2, 2, 2]), set())
        self.assertEqual(ne_na_lihih([]), set())
        self.assertEqual(ne_na_lihih([12, 17, 17, 5, 18, 9, 9, 18]), {12})


class Naloga_2_Intervali(unittest.TestCase):
    def test_intervali(self):
        self.assertEqual(intervali([1, 2, 3, 4]), [(1, 4)])
        self.assertEqual(intervali([1, 2, 3, 4, 8, 9, 10]), [(1, 4), (8, 10)])
        self.assertEqual(intervali([8, 9, 10, 1, 2, 3, 4]), [(8, 10), (1, 4)])
        self.assertEqual(intervali([1, 2, 3, 4, 8, 9, 10, 20]), [(1, 4), (8, 10), (20, 20)])
        self.assertEqual(intervali([1, 2, 3, 4, 6, 8, 9, 10]), [(1, 4), (6, 6), (8, 10)])
        self.assertEqual(intervali([-1, 1, 2, 3, 4, 8, 9, 10]), [(-1, -1), (1, 4), (8, 10)])
        self.assertEqual(intervali([1, 5, 9]), [(1, 1), (5, 5), (9, 9)])
        self.assertEqual(intervali([1, 3, 5, 7, 9]), [(1, 1), (3, 3), (5, 5), (7, 7), (9, 9)])
        self.assertEqual(intervali([]), [])

    def test_razpisi(self):
        self.assertEqual(razpisi([(1, 4)]), [1, 2, 3, 4])
        self.assertEqual(razpisi([(1, 4), (8, 10)]), [1, 2, 3, 4, 8, 9, 10])
        self.assertEqual(razpisi([(1, 4), (8, 10), (20, 20)]),
                         [1, 2, 3, 4, 8, 9, 10, 20])
        self.assertEqual(razpisi([(1, 4), (6, 6), (8, 10)]),
                         [1, 2, 3, 4, 6, 8, 9, 10])
        self.assertEqual(razpisi([(-1, -1), (1, 4), (8, 10)]),
                         [-1, 1, 2, 3, 4, 8, 9, 10])
        self.assertEqual(razpisi([(1, 1), (5, 5), (9, 9)]), [1, 5, 9])
        self.assertEqual(razpisi([]), [])


class Naloga_3_Indeksi(unittest.TestCase):
    def test_indeksi_rec(self):
        with self.assertRaises(RecursionError,
                               msg="Funkcija mora biti rekurzivna"):
            indeksi_rec(list(range(2000)), 0)
        self.assertEqual(indeksi_rec([5, 6, 1, 2], 1), [2])
        self.assertEqual(indeksi_rec([1, 5, 6, 1, 2], 1), [0, 3])
        self.assertEqual(indeksi_rec([1, 5, 6, 1, 1, 2], 1), [0, 3, 4])
        self.assertEqual(indeksi_rec([1, 1, 1], 1), [0, 1, 2])
        self.assertEqual(indeksi_rec([1], 1), [0])
        self.assertEqual(indeksi_rec([], 1), [])
        self.assertEqual(indeksi_rec([2, 3, 4], 1), [])

        self.assertEqual(indeksi_rec(["Ana", "Berta", "Cilka", "Berta"], "Berta"), [1, 3])
        self.assertEqual(indeksi_rec(["Ana", "Berta", "Cilka", "Berta"], "Dani"), [])

    def test_indeksi_gen(self):
        self.assertEqual(indeksi_gen([5, 6, 1, 2], 1), [2])
        self.assertEqual(indeksi_gen([1, 5, 6, 1, 2], 1), [0, 3])
        self.assertEqual(indeksi_gen([1, 5, 6, 1, 1, 2], 1), [0, 3, 4])
        self.assertEqual(indeksi_gen([1, 1, 1], 1), [0, 1, 2])
        self.assertEqual(indeksi_gen([1], 1), [0])
        self.assertEqual(indeksi_gen([], 1), [])
        self.assertEqual(indeksi_gen([2, 3, 4], 1), [])

        self.assertEqual(indeksi_gen(["Ana", "Berta", "Cilka", "Berta"], "Berta"), [1, 3])
        self.assertEqual(indeksi_gen(["Ana", "Berta", "Cilka", "Berta"], "Dani"), [])


class Naloga_4_Predelaj(unittest.TestCase):
    def test_sopomena(self):
        sinonimi = [{"fant", "deček", "pob"},
                    {"dekle", "punca"},
                    {"cesta", "pot", "kolovoz", "makadam"},
                    {"kis", "jesih"},
                    {"noge", "tace"}]

        stavek = "pob in dekle sta vzela pot pod noge"
        pob, in_, dekle, sta, vzela, pot, pod, noge = predelaj(stavek, sinonimi).split()
        self.assertIn(pob, {"deček", "fant"})
        self.assertEqual(in_, "in")
        self.assertEqual(dekle, "punca")
        self.assertEqual(sta, "sta")
        self.assertEqual(vzela, "vzela")
        self.assertIn(pot, {"cesta", "kolovoz", "makadam"})
        self.assertEqual(pod, "pod")
        self.assertEqual(noge, "tace")

        stavek = "pob in punca sta vzela cesta pod tace"
        pob, in_, punca, sta, vzela, cesta, pod, tace = predelaj(stavek, sinonimi).split()
        self.assertIn(pob, {"deček", "fant"})
        self.assertEqual(in_, "in")
        self.assertEqual(punca, "dekle")
        self.assertEqual(sta, "sta")
        self.assertEqual(vzela, "vzela")
        self.assertIn(cesta, {"pot", "kolovoz", "makadam"})
        self.assertEqual(pod, "pod")
        self.assertEqual(tace, "noge")


class Naloga_5_PicerijaNaZalogo(unittest.TestCase):
    def test_1_init_len(self):
        p = PicerijaNaZalogo()
        self.assertEqual(len(p), 0)

    def test_2_speci_str(self):
        p = PicerijaNaZalogo()
        q = PicerijaNaZalogo()
        p.speci("margerita")
        self.assertEqual(len(p), 1)
        self.assertEqual(len(q), 0)
        self.assertEqual(str(p), "margerita")
        p.speci("margerita")
        p.speci("siri")
        self.assertEqual(len(p), 3)
        self.assertEqual(str(p), "margerita, siri")
        p.speci("klasika")
        self.assertEqual(len(p), 4)
        self.assertEqual(str(p), "klasika, margerita, siri")
        self.assertEqual(len(q), 0)
        self.assertEqual(str(q), "")
        q.speci("klasika")
        self.assertEqual(len(p), 4)
        self.assertEqual(str(p), "klasika, margerita, siri")
        self.assertEqual(len(q), 1)
        self.assertEqual(str(q), "klasika")

    def test_3_prodaj_zasluzek(self):
        p = PicerijaNaZalogo()
        q = PicerijaNaZalogo()
        self.assertEqual(p.zasluzek(), 0)
        p.speci("margerita")
        self.assertEqual(len(p), 1)
        self.assertEqual(len(q), 0)
        self.assertEqual(str(p), "margerita")
        self.assertEqual(p.zasluzek(), 0)
        p.speci("margerita")
        p.speci("siri")
        self.assertEqual(len(p), 3)
        self.assertEqual(str(p), "margerita, siri")
        self.assertEqual(p.zasluzek(), 0)
        p.prodaj("margerita")
        self.assertEqual(len(p), 2)
        self.assertEqual(str(p), "margerita, siri")
        self.assertEqual(p.zasluzek(), 1)
        p.prodaj("margerita")
        self.assertEqual(len(p), 1)
        self.assertEqual(str(p), "siri")
        self.assertEqual(p.zasluzek(), 2)
        p.speci("klasika")
        self.assertEqual(len(p), 2)
        self.assertEqual(str(p), "klasika, siri")
        self.assertEqual(p.zasluzek(), 2)
        p.prodaj("margerita")
        self.assertEqual(len(p), 2)
        self.assertEqual(str(p), "klasika, siri")
        self.assertEqual(p.zasluzek(), 2)
        p.speci("zelenjavna")
        p.prodaj("klasika")
        self.assertEqual(p.zasluzek(), 4)
        p.prodaj("siri")
        self.assertEqual(p.zasluzek(), 7)
        p.prodaj("zelenjavna")
        self.assertEqual(p.zasluzek(), 8)

if __name__ == "__main__":
    unittest.main()
