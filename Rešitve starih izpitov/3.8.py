#Izpit 2015/16 15.februar

from collections import defaultdict

def bomboniera(sirina,visina,pojedeno):
    stoplci = set()
    vrstice = set()
    if pojedeno:
        for koord in pojedeno:
            x,y = koord
            if x not in stoplci:
                sirina -= 1
            if y not in vrstice:
                visina -= 1
            stoplci.add(x)
            vrstice.add(x)
        return sirina * visina
    return sirina * visina


def izpis_vrstice(kraj,vreme,temperatura,veter,tlak):

    return f"{kraj:35}{vreme:>20}{temperatura:5}{veter:5}{tlak:8}"


def izpisi_vreme(datoteka):
    s = []
    file = open(datoteka, encoding="utf8")
    for vrstica in file:
        podatki = vrstica.strip().split("\t")
        podatki = (podatki + 5 * [""])[:5]
        kraj,vreme = podatki[:2]
        temperatura, veter, tlak = [int(x) if x else "" for x in podatki[2:]]
        s.append(izpis_vrstice(kraj, vreme, temperatura, veter, tlak))
    return "\n".join(s)


def prafaktorji(n):
    _prafaktorji = defaultdict(int)
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                _prafaktorji[i] += 1
                break
    return _prafaktorji


def gcd(a,b):
    skupni = 1
    for sta in a:
        for stb in b:
            if sta == stb:
                if a[sta] > b[stb]:
                    skupni *= stb**b[stb]
                elif a[sta] < b[stb]:
                    skupni *= sta**a[sta]
    return skupni

def najm_praf(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i

def prafaktorji_rec(n):
    np = najm_praf(n)
    if np != n:
        ostali = prafaktorji_rec(n // np)
        ostali[np] += 1
        return ostali
    else:
        ostali = defaultdict(int)
    ostali[np] += 1
    return ostali

# Rekurzija: Najprej določimo kako se bo rekurzija končala.
# Ne večkrat klicat rekurzivnih klicou v funkciji, ker čene bo rekurzija prepočasna

class PisniIzdelek:

    def __init__(self, ime):
        self.ime = ime
        self.tocke_pri_nalogah = {1: None, 2: None, 3: None, 4: None, 5: None}

    def daj_tocke(self, naloga, tocke):
        self.tocke_pri_nalogah[naloga] = tocke

    def rezultat(self):
        tocke = [self.tocke_pri_nalogah[naloga] for naloga in self.tocke_pri_nalogah]
        return (self.ime,tuple(tocke))

    def vsota(self):
        return sum(self.tocke_pri_nalogah[naloga] for naloga in self.tocke_pri_nalogah
                   if self.tocke_pri_nalogah[naloga] != None)

    def naredil(self):
        if self.vsota() >= 50:
            return True
        else:
            return False

    def ocena(self):
        if self.vsota():
            if self.vsota() < 50:
                return 5
            elif 50 <= self.vsota() <= 59:
                return 6
            elif 60 <= self.vsota() <= 69:
                return 7
            elif 70 <= self.vsota() <= 79:
                return 8
            elif 80 <= self.vsota() <= 89:
                return 9
            elif 90 <= self.vsota() <= 100:
                return 10
        else:
            return 5


import unittest

class Test01Bomboniera(unittest.TestCase):
    def test_bomboniera(self):
        self.assertEqual(bomboniera(3, 5, []), 15)
        self.assertEqual(bomboniera(3, 5, [(1, 1)]), 8)
        self.assertEqual(bomboniera(3, 5, [(1, 2)]), 8)
        self.assertEqual(bomboniera(8, 5, [(1, 3), (1, 7)]), 21)
        self.assertEqual(bomboniera(8, 5, [(1, 3), (3, 7)]), 18)
        self.assertEqual(bomboniera(8, 5, [(1, 1), (1, 2), (1, 3), (1, 4)]), 7)
        self.assertEqual(bomboniera(5, 8, [(1, 1), (1, 2), (1, 3), (1, 4)]), 16)
        self.assertEqual(bomboniera(8, 5, [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]), 0)
        self.assertEqual(bomboniera(1, 1, []), 1)
        self.assertEqual(bomboniera(1, 1, [(1, 1)]), 0)


class Test02Vreme(unittest.TestCase):
    def test_izpis_vrstice(self):
        self.assertEqual(
            izpis_vrstice('Bilje pri Novi Gorici', 'oblačno', 9, 9, 997),
            'Bilje pri Novi Gorici                           oblačno    9    9     997')
        self.assertEqual(
            izpis_vrstice('Celje', 'pretežno jasno', 6, 9, 997),
            'Celje                                    pretežno jasno    6    9     997')
        self.assertEqual(
            izpis_vrstice('Črnomelj', '', 12, 8, 996),
            'Črnomelj                                                  12    8     996')
        self.assertEqual(
            izpis_vrstice('Kredarica', 'delno oblačno', -8, 15, 728),
            'Kredarica                                 delno oblačno   -8   15     728')
        self.assertEqual(
            izpis_vrstice('Letališče Cerklje ob Krki', 'pretežno jasno', 9, 13, 996),
            'Letališče Cerklje ob Krki                pretežno jasno    9   13     996')
        self.assertEqual(
            izpis_vrstice('Letališče Edvarda Rusjana Maribor', 'pretežno jasno', 9, 12, 996),
            'Letališče Edvarda Rusjana Maribor        pretežno jasno    9   12     996')
        self.assertEqual(
            izpis_vrstice('Letališče Jožeta Pučnika Ljubljana', 'megla', 2, 6, 998),
            'Letališče Jožeta Pučnika Ljubljana                megla    2    6     998')
        self.assertEqual(
            izpis_vrstice('Letališče Lesce', '', 2, 6, 998),
            'Letališče Lesce                                            2    6     998')
        self.assertEqual(
            izpis_vrstice('Letališče Portorož', 'delno oblačno', 8, 19, 998),
            'Letališče Portorož                        delno oblačno    8   19     998')
        self.assertEqual(
            izpis_vrstice('Ljubljana', 'megla v okolici', 4, 5, 998),
            'Ljubljana                               megla v okolici    4    5     998')
        self.assertEqual(
            izpis_vrstice('Murska Sobota', 'zmerno oblačno', 6, 4, 996),
            'Murska Sobota                            zmerno oblačno    6    4     996')
        self.assertEqual(
            izpis_vrstice('Novo mesto', 'pretežno jasno', 8, 7, 997),
            'Novo mesto                               pretežno jasno    8    7     997')
        self.assertEqual(
            izpis_vrstice('Postojna', '', 4, 4, ''),
            'Postojna                                                   4    4        ')
        self.assertEqual(
            izpis_vrstice('Rateče', 'jasno', 5, 0, 900),
            'Rateče                                            jasno    5    0     900')
        self.assertEqual(
            izpis_vrstice('Slovenj Gradec', 'pretežno jasno', 5, '', ''),
            'Slovenj Gradec                           pretežno jasno    5             ')

    def test_izpisi_vreme(self):
        self.assertEqual(
            izpisi_vreme("vreme.txt"),
            "Bilje pri Novi Gorici                           oblačno    9    9     997\n"
            "Celje                                    pretežno jasno    6    9     997\n"
            "Črnomelj                                                  12    8     996\n"
            "Kredarica                                 delno oblačno   -8   15     728\n"
            "Letališče Cerklje ob Krki                pretežno jasno    9   13     996\n"
            "Letališče Edvarda Rusjana Maribor        pretežno jasno    9   12     996\n"
            "Letališče Jožeta Pučnika Ljubljana                megla    2    6     998\n"
            "Letališče Lesce                                            2    6     998\n"
            "Letališče Portorož                        delno oblačno    8   19     998\n"
            "Ljubljana                               megla v okolici    4    5     998\n"
            "Murska Sobota                            zmerno oblačno    6    4     996\n"
            "Novo mesto                               pretežno jasno    8    7     997\n"
            "Postojna                                                   4    4        \n"
            "Rateče                                            jasno    5    0     900\n"
            "Slovenj Gradec                           pretežno jasno    5             ")


class Test03Prafaktorji(unittest.TestCase):
    def test_prafaktorji(self):
        self.assertEqual(prafaktorji(42), {2: 1, 3: 1, 7: 1})
        self.assertEqual(prafaktorji(5), {5: 1})
        self.assertEqual(prafaktorji(8), {2: 3})
        self.assertEqual(prafaktorji(256), {2: 8})
        self.assertEqual(prafaktorji(768), {2: 8, 3: 1})
        self.assertEqual(prafaktorji(2), {2: 1})

    def test_gcd(self):
        self.assertEqual(gcd({5: 2, 3: 5}, {5: 1, 7: 2}), 5)
        self.assertEqual(gcd({5: 2, 3: 5}, {5: 1, 3: 2, 7: 2},), 45)
        self.assertEqual(gcd({5: 2, 3: 5}, {7: 2, 11: 1},), 1)

        self.assertEqual(gcd({452930477: 3, 472882027: 6, 920419813: 4},
                             {452930477: 2, 472882027: 7, 961748941: 2}),
                         2293928816117585439086142495441970950689484275718088538073075344497681)


class Test04PrafaktorjiRec(unittest.TestCase):
    def test_prafaktorji_rec(self):
        self.assertEqual(prafaktorji_rec(42), {2: 1, 3: 1, 7: 1})
        self.assertEqual(prafaktorji_rec(5), {5: 1})
        self.assertEqual(prafaktorji_rec(8), {2: 3})
        self.assertEqual(prafaktorji_rec(256), {2: 8})
        self.assertEqual(prafaktorji_rec(768), {2: 8, 3: 1})


class Test05PisniIzdelek(unittest.TestCase):
    def test_pisni_izdelek(self):
        ana = PisniIzdelek("Ana Novak")
        benjamin = PisniIzdelek("Benjamin Briten")

        self.assertEqual(ana.rezultat(), ("Ana Novak", (None, None, None, None, None)))
        self.assertEqual(ana.vsota(), 0)
        self.assertEqual(ana.ocena(), 5)
        self.assertFalse(ana.naredil())
        self.assertEqual(benjamin.rezultat(), ("Benjamin Briten", (None, None, None, None, None)))
        self.assertEqual(benjamin.vsota(), 0)
        self.assertEqual(benjamin.ocena(), 5)
        self.assertFalse(benjamin.naredil())

        ana.daj_tocke(2, 20)

        self.assertEqual(ana.rezultat(), ("Ana Novak", (None, 20, None, None, None)))
        self.assertEqual(ana.vsota(), 20)
        self.assertEqual(ana.ocena(), 5)
        self.assertFalse(ana.naredil())
        self.assertEqual(benjamin.rezultat(), ("Benjamin Briten", (None, None, None, None, None)))
        self.assertEqual(benjamin.vsota(), 0)
        self.assertEqual(benjamin.ocena(), 5)
        self.assertFalse(benjamin.naredil())

        ana.daj_tocke(5, 10)

        self.assertEqual(ana.rezultat(), ("Ana Novak", (None, 20, None, None, 10)))
        self.assertEqual(ana.vsota(), 30)
        self.assertEqual(ana.ocena(), 5)
        self.assertFalse(ana.naredil())
        self.assertEqual(benjamin.rezultat(), ("Benjamin Briten", (None, None, None, None, None)))
        self.assertEqual(benjamin.vsota(), 0)
        self.assertEqual(benjamin.ocena(), 5)
        self.assertFalse(benjamin.naredil())

        ana.daj_tocke(1, 19)

        self.assertEqual(ana.rezultat(), ("Ana Novak", (19, 20, None, None, 10)))
        self.assertEqual(ana.vsota(), 49)
        self.assertEqual(ana.ocena(), 5)
        self.assertFalse(ana.naredil())
        self.assertEqual(benjamin.rezultat(), ("Benjamin Briten", (None, None, None, None, None)))
        self.assertEqual(benjamin.vsota(), 0)
        self.assertEqual(benjamin.ocena(), 5)
        self.assertFalse(benjamin.naredil())

        ana.daj_tocke(3, 1)

        self.assertEqual(ana.rezultat(), ("Ana Novak", (19, 20, 1, None, 10)))
        self.assertEqual(ana.vsota(), 50)
        self.assertEqual(ana.ocena(), 6)
        self.assertTrue(ana.naredil())
        self.assertEqual(benjamin.rezultat(), ("Benjamin Briten", (None, None, None, None, None)))
        self.assertEqual(benjamin.vsota(), 0)
        self.assertEqual(benjamin.ocena(), 5)
        self.assertFalse(benjamin.naredil())

        ana.daj_tocke(4, 9)

        self.assertEqual(ana.rezultat(), ("Ana Novak", (19, 20, 1, 9, 10)))
        self.assertEqual(ana.vsota(), 59)
        self.assertEqual(ana.ocena(), 6)
        self.assertTrue(ana.naredil())
        self.assertEqual(benjamin.rezultat(), ("Benjamin Briten", (None, None, None, None, None)))
        self.assertEqual(benjamin.vsota(), 0)
        self.assertEqual(benjamin.ocena(), 5)
        self.assertFalse(benjamin.naredil())

        ana.daj_tocke(1, 20)

        self.assertEqual(ana.rezultat(), ("Ana Novak", (20, 20, 1, 9, 10)))
        self.assertEqual(ana.vsota(), 60)
        self.assertEqual(ana.ocena(), 7)
        self.assertTrue(ana.naredil())
        self.assertEqual(benjamin.rezultat(), ("Benjamin Briten", (None, None, None, None, None)))
        self.assertEqual(benjamin.vsota(), 0)
        self.assertEqual(benjamin.ocena(), 5)
        self.assertFalse(benjamin.naredil())

        ana.daj_tocke(3, 20)
        ana.daj_tocke(4, 20)
        ana.daj_tocke(5, 20)

        self.assertEqual(ana.rezultat(), ("Ana Novak", (20, 20, 20, 20, 20)))
        self.assertEqual(ana.vsota(), 100)
        self.assertEqual(ana.ocena(), 10)
        self.assertTrue(ana.naredil())
        self.assertEqual(benjamin.rezultat(), ("Benjamin Briten", (None, None, None, None, None)))
        self.assertEqual(benjamin.vsota(), 0)
        self.assertEqual(benjamin.ocena(), 5)
        self.assertFalse(benjamin.naredil())


if __name__ == "__main__":
    unittest.main()



