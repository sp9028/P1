import math
from collections import Counter


def pecivo(s):
    return 3 * s.count("A") - len(s)


def najmanjsi_unikat(s):
    stevci = Counter(s)
# Counter vrne slovar z ključem elementov in stevilko ponovitve vsakega elementa
# sorted sortira elemente po velikosti
    for el in sorted(stevci):
        if stevci[el] == 1:
            return el


def neprazne(ime_datoteke):
    prazne = 0
    vse = 0
    for vrstica in open(ime_datoteke):
        if len(vrstica.strip()) == 0:
            prazne += 1
        vse += 1
    return vse - prazne


def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        n /= 2
        return 1 + collatz(n)
    else:
        n = n * 3 + 1
        return 1 + collatz(n)


class Ladja:
    smeri = ["sever","vzhod","jug","zahod"]

    def __init__(self):
        self.pozicija = (0,0)
        self.hitrost = 0
        self.smer = "sever"
        self.dolzina = 0

    def kje_si(self):
        return self.pozicija

    def premikaj(self,cas):
        prejsnja = self.pozicija
        x,y = self.pozicija
        if self.smer == "sever":
            y += self.hitrost * cas
        elif self.smer == "jug":
            y -= self.hitrost * cas
        elif self.smer == "vzhod":
            x += self.hitrost * cas
        else:
            x -= self.hitrost * cas
        self.pozicija = x,y
        self.dolzina += math.sqrt((x - prejsnja[0]) ** 2 + (y - prejsnja[1]) ** 2)

    def spremeni_hitrost(self, koliko):
        self.hitrost += koliko

    def obrni(self, kam):
        if kam == "L":
            self.smer = self.smeri[self.smeri.index(self.smer) - 1]
        else:
            if self.smer == self.smeri[-1]:
                self.smer = self.smeri[0]
            else:
                self.smer = self.smeri[self.smeri.index(self.smer) + 1]

# skozi list gres lahko levo brez dodatnih pogojev nemores pa desno saj bo index out of range

    def dolzina_poti(self):
        return self.dolzina



import unittest


class Test01Preste(unittest.TestCase):
    def test_preste(self):
        self.assertEqual(pecivo("AAABAABOAABO"), 9)
        self.assertEqual(pecivo("ABO"), 0)
        self.assertEqual(pecivo("A"), 2)
        self.assertEqual(pecivo("AB"), 1)
        self.assertEqual(pecivo("AA"), 4)
        self.assertEqual(pecivo(""), 0)


class Test02NajmanjsiUnikat(unittest.TestCase):
    def test_najunikat(self):
        self.assertEqual(najmanjsi_unikat([1, 2, 3]), 1)
        self.assertEqual(najmanjsi_unikat([2, 1, 3]), 1)
        self.assertEqual(najmanjsi_unikat([2, 3, 1]), 1)
        self.assertEqual(najmanjsi_unikat(["Berta", "Ana", "Cilka"]), "Ana")

        self.assertEqual(najmanjsi_unikat([3, 1, 2, 2, 1, 2, 4]), 3)

        self.assertIsNone(najmanjsi_unikat([]))
        self.assertIsNone(najmanjsi_unikat([2, 2]))
        self.assertIsNone(najmanjsi_unikat([2, 3, 2, 3]))


# Pripravimo datoteke, da bodo ostale tudi po testih in se bo študent lahko
# igral z njimi

import warnings
warnings.filterwarnings("ignore", category=ResourceWarning)

open("tri-neprazne.txt", "wt").write(
    """prva


    druga
    tretja

    """)

open("se-tri-neprazne.txt", "wt").write(
    """prva


    druga
    tretja
    """)

open("in-se-tri-neprazne.txt", "wt").write(
    """prva


    druga
    tretja""")

open("pet.txt", "wt", encoding="utf8").write(
    """prva vrstica je tu
    druga tu
    pa se tretja
    cetrta!
    in pa peta!""")

open("prazno.txt", "wt")

open("tudi-prazno.txt", "wt").write("""



""")


class Test03Neprazne(unittest.TestCase):
    def test_neprazne(self):
        warnings.filterwarnings("ignore", category=ResourceWarning)
        self.assertEqual(neprazne("tri-neprazne.txt"), 3)
        self.assertEqual(neprazne("se-tri-neprazne.txt"), 3)
        self.assertEqual(neprazne("in-se-tri-neprazne.txt"), 3)
        self.assertEqual(neprazne("pet.txt"), 5)
        self.assertEqual(neprazne("prazno.txt"), 0)
        self.assertEqual(neprazne("tudi-prazno.txt"), 0)


class Test04Collatz(unittest.TestCase):
    def test_collatz(self):
        self.assertEqual(collatz(42), 9)
        self.assertEqual(collatz(8), 4)
        self.assertEqual(collatz(1), 1)
        self.assertEqual(collatz(15), 18)
        self.assertEqual(collatz(152), 24)


class Test05Ladja(unittest.TestCase):
    def test_ladja(self):
        ladja = Ladja()
        self.assertEqual(ladja.kje_si(), (0, 0))

        ladja.premikaj(5)  # Ne gremo nikamor, saj je hitrost enaka 0
        self.assertEqual(ladja.kje_si(), (0, 0))

        ladja.spremeni_hitrost(4)  # Spremenili smo hitrost, vendar se ne premikamo
        self.assertEqual(ladja.kje_si(), (0, 0))

        ladja.premikaj(5)
        # 5 casovnih enot se premikamo s hitrostjo 4, torej se premaknemo za 5 * 4 = 20
        # Premikamo pa se na sever, torej se poveča y
        self.assertEqual(ladja.kje_si(), (0, 20))

        ladja.obrni("D")  # Obrnemo se na vzhod
        # Če se le obrnemo, se zato še ne premaknemo...
        self.assertEqual(ladja.kje_si(), (0, 20))

        ladja.premikaj(1)  # Zdaj gremo proti vzhodu - povečujemo x
        self.assertEqual(ladja.kje_si(), (4, 20))

        ladja.obrni("D")  # proti jugu
        ladja.obrni("D")  # proti zahodu
        ladja.spremeni_hitrost(-1)  # zdaj je hitrost enaka 4 - 1 = 3
        ladja.premikaj(2)  # tako da se premaknemo za 6, a v levo -> x se manjša
        self.assertEqual(ladja.kje_si(), (-2, 20))

        ladja.obrni("D")  # spet na sever
        ladja.premikaj(2)
        self.assertEqual(ladja.kje_si(), (-2, 26))

        ladja.obrni("L")  # zahod
        ladja.premikaj(2)
        self.assertEqual(ladja.kje_si(), (-8, 26))

        ladja.obrni("L")  # jug
        ladja.obrni("L")  # vzhod
        ladja.obrni("L")  # sever
        ladja.premikaj(2)
        self.assertEqual(ladja.kje_si(), (-8, 32))

        self.assertEqual(ladja.dolzina_poti(), 48)


if __name__ == "__main__":
    unittest.main()

