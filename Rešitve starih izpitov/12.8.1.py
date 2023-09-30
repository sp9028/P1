import unittest
import random


def menjave(razpored, zamenjave):
    prva_mesta = set()
    prva_mesta.add(razpored[0])
    for prvi,drugi in zamenjave:
        prej = razpored[prvi]
        razpored[prvi] = razpored[drugi]
        razpored[drugi] = prej
        prva_mesta.add(razpored[0])
    return prva_mesta


def najblizji_par(s):
    razlike = {}
    for i in range(len(s)):
        for k in range(len(s)):
            if i != k and s[i] < s[k]:
                razlike[(s[i], s[k])] = abs(s[i] - s[k])
    # Tako vrnemo minimalen ključ z minimalno vrednostjo kar v eneme returnu
    return min([par for par in razlike if razlike[par] == min(razlike.values())])


def pari(s):
    sez = []
    while len(s) > 1:
        par = najblizji_par(s)
        sez.append(par)
        st1,st2 = par
        s.remove(st1)
        s.remove(st2)
    return sez


def bomboni(s,t):
    odprti_bomboni = set()
    a = 0
    b = 0
    for ana,berta in zip(s,t):
        if ana != berta:
            if ana not in odprti_bomboni:
                a += 1
                odprti_bomboni.add(ana)
            if berta not in odprti_bomboni:
                b += 1
                odprti_bomboni.add(berta)
        else:
            odprti_bomboni.add(ana)
    return (a + len(set(s[len(t):]) - odprti_bomboni),
            b + len(set(t[len(s):]) - odprti_bomboni))


def izmenicna_vsota(s):
    if not s:
        return 0
    elif len(s) == 1:
        return s[0]
    else:
        return s[0] - s[1] + izmenicna_vsota(s[2:])

# 1. BASE CASE sepravi kdaj se rekurzija konca. Potem pa naprej razdelimo problem na majhne problemcke


class Naloge:

    def __init__(self):
        self.naloge = {}
        self.stevilo_zamujenih = 0

    def dodaj(self, ime_naloge, rok):
        self.naloge[ime_naloge] = rok

    def opravi(self,ime_naloge, cas):
        # da imajo slovarji metodo pop, ki ji podamo ključ in vrne pripadajočo vrednost,
        # mimogrede pa ju še pobriše iz slovarja
        rok = self.naloge.pop(ime_naloge)
        if cas > rok:
            self.stevilo_zamujenih += 1

    def naslednja_naloga(self):
        if self.naloge:
            return min(self.naloge, key=self.naloge.get)

    def cakajocih(self):
        return len(self.naloge)

    def zamujenih(self):
        return self.stevilo_zamujenih



class Test(unittest.TestCase):
    def test_menjave(self):
        razpored = ["Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči", "Greta"]
        na0 = menjave(razpored, [(0, 4)])
        self.assertEqual(["Ema", "Berta", "Cilka", "Dani", "Ana", "Fanči", "Greta"], razpored)
        self.assertEqual({"Ana", "Ema"}, na0)

        razpored = ["Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči", "Greta"]
        na0 = menjave(razpored, [(0, 4), (1, 2), (0, 2)])
        self.assertEqual(["Berta", "Cilka", "Ema", "Dani", "Ana", "Fanči", "Greta"], razpored)
        self.assertEqual({"Ana", "Ema", "Berta"}, na0)

        razpored = ["Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči", "Greta"]
        na0 = menjave(razpored, [])
        self.assertEqual(["Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči", "Greta"], razpored)
        self.assertEqual({"Ana"}, na0)

    def test_pari(self):
        self.assertEqual((5, 7), najblizji_par([2, -2, 5, 10, 7, 20]))
        self.assertEqual((5, 7), najblizji_par([2, -2, 7, 10, 5, 20]))
        self.assertEqual((-4, -2), najblizji_par([-4, -2, 7, 10, 5, 20]))
        self.assertEqual((-4, -2), najblizji_par([7, 10, -4, -2, 5, 20]))
        self.assertEqual((-4, -2), najblizji_par([7, 10, -4, 5, 20, -2]))
        self.assertEqual((-4, -2), najblizji_par([7, 10, -4, 5, 20, -2]))
        s = [7, 10, -4, 5, 20, -2]
        for _ in range(100):
            random.shuffle(s)
            self.assertEqual((-4, -2), najblizji_par(s), f"Napaka pri f{s}")
        self.assertEqual((5, 6.5), najblizji_par([2, -2, 5, 6.5, 10, 20]))
        self.assertEqual((5, 6.5), najblizji_par([2, -2, 6.5, 5, 10, 20]))

        self.assertEqual([(5, 6.5), (-2, 2), (10, 20)], pari([2, 5, 6.5, -2, 10, 20]))
        self.assertEqual([(5, 6.5), (-2, 2)], pari([2, 5, 6.5, -2, 10]))

    def test_zmage(self):
        s = [4, 1, 4, 7, 4, 3, 5, 6, 8, 5, 3, 2, 4, 6]
        t = [1, 3, 5, 4, 6, 1, 2]
        self.assertEqual((3, 5), bomboni(s, t))
        self.assertEqual((5, 3), bomboni(t, s))

        s = [4, 1, 2, 4, 7, 4, 3, 5, 6, 8, 5, 3, 2, 4, 6]
        t = [1, 3, 2, 5, 4, 6, 1, 2]
        self.assertEqual((3, 4), bomboni(s, t))

        s = [random.randint(1, 10000) for _ in range(10000)]
        t = [random.randint(1, 10000) for _ in range(10000)]
        bomboni(s, t)

    def test_izmenicna_vsota(self):
        self.assertEqual(0, izmenicna_vsota([]), 0)
        self.assertEqual(42, izmenicna_vsota([42]))
        self.assertEqual(42 - 5, izmenicna_vsota([42, 5]))
        self.assertEqual(4 - 1 + 7 - 3 + 6 - 1 + 7 - 6,
                         izmenicna_vsota([4, 1, 7, 3, 6, 1, 7, 6]))
        self.assertEqual(4 - 1 + 7 - 3 + 6 - 1 + 7 - 6 + 5,
                         izmenicna_vsota([4, 1, 7, 3, 6, 1, 7, 6, 5]))

    def test_opravila(self):
        opravila = Naloge()
        self.assertIsNone(opravila.naslednja_naloga())
        self.assertEqual(0, opravila.zamujenih())
        self.assertEqual(0, opravila.cakajocih())

        self.assertIsNone(opravila.dodaj("A", 42))
        opravila.dodaj("B", 30)
        opravila.dodaj("C", 50)
        opravila.dodaj("D", 35)
        self.assertEqual("B", opravila.naslednja_naloga())
        self.assertEqual(0, opravila.zamujenih())
        self.assertEqual(4, opravila.cakajocih())

        self.assertIsNone(opravila.opravi("D", 33))
        self.assertEqual("B", opravila.naslednja_naloga())
        self.assertEqual(0, opravila.zamujenih())
        self.assertEqual(3, opravila.cakajocih())

        opravila.opravi("B", 37)
        self.assertEqual("A", opravila.naslednja_naloga())
        self.assertEqual(1, opravila.zamujenih())
        self.assertEqual(2, opravila.cakajocih())

        opravila.dodaj("D", 40)
        self.assertEqual("D", opravila.naslednja_naloga())
        self.assertEqual(1, opravila.zamujenih())
        self.assertEqual(3, opravila.cakajocih())

        opravila.opravi("A", 42)
        self.assertEqual("D", opravila.naslednja_naloga())
        self.assertEqual(1, opravila.zamujenih())
        self.assertEqual(2, opravila.cakajocih())


if __name__ == "__main__":
    unittest.main()

