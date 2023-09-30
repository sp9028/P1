import unittest
from collections import defaultdict


def stisni(s):
    sez = []
    c = ""
    st = 0
    for i in range(len(s)):
        if s[i] != c:
            if st != 0:
                sez.append(str(st) + c)
            st = 1
            c = s[i]
        else:
            st += 1

        if i == len(s) - 1:
            sez.append(str(st) + c)

    return " ".join(sez)


def razsiri(s):
    sez = []
    for niz in s.split():
        sez.append(int(niz[:-1]) * niz[-1])
    return "".join(sez)

# ZELO LEPA REŠITEV! Stringe lahko množimo z številkami. Sepravi 4 * "a" = "aaaa"


def lzw_stisni(s, kode):
    nov_niz = []
    for crka in s:
        for koda in kode:
            if crka == koda:
                nov_niz.append(kode[koda])
                break
    return "".join(nov_niz)

# Replace naredi samo trenutno operacijo in se shranjuje rezultata sproti. Mogel bi vsakič definirati novo var
# če bi to hotel


def lzw_razsiri(s, kode):
    trenutna_koda = ""
    niz = []
    for st in s:
        trenutna_koda += st
        for koda in kode:
            if kode[koda] == trenutna_koda:
                niz.append(koda)
                trenutna_koda = ""
                break
    return "".join(niz)


def odkodiraj(n, s):
    for st in n:
        s = s[int(st)] # Listi se lahko takole inicalizirajo
    return s


def odkodiraj_rek(koda, kode):
    if koda:
        return odkodiraj(koda[1:], kode[int(koda[0])])
    else:
        return kode


class Kodirnik:

    def __init__(self):
        self._kode = {}
        self.stevilka = 0
        self.txt = []
        self.zakodiran_txt = []

    def dodaj(self, znak):
        self.txt.append(znak)
        if znak not in self._kode.keys():
            self._kode[znak] = self.stevilka
            self.stevilka += 1
        self.zakodiran_txt.append(self._kode[znak])

    def kodirano(self):
        return self.zakodiran_txt

    def kode(self):
        # Če imamo terke v tem primeru zazipana seznama lahko to spremenimo v DICT in bo prvi element kljuc,
        # drug pa vrednost
        return dict(zip(self.txt, self.zakodiran_txt))

    def znaki(self):
        return dict(zip(self.zakodiran_txt, self.txt))

class Test01Zip(unittest.TestCase):
    def test_stisni(self):
        self.assertEqual(stisni("AAAATTCGGGG"), "4A 2T 1C 4G")
        self.assertEqual(stisni("AAAATTCG"), "4A 2T 1C 1G")
        self.assertEqual(stisni("AAAA"), "4A")
        self.assertEqual(stisni("AAAATTTAAA"), "4A 3T 3A")
        self.assertEqual(stisni(""), "")
        self.assertEqual(stisni("GCTAG"), "1G 1C 1T 1A 1G")
        self.assertEqual(stisni(14 * "A" + 100 * "G" + "AAC"), "14A 100G 2A 1C")

    def test_razsiri(self):
        self.assertEqual(razsiri("4A 2T 1C 4G"), "AAAATTCGGGG")
        self.assertEqual(razsiri("4A 2T 1C 1G"), "AAAATTCG")
        self.assertEqual(razsiri("4A"), "AAAA")
        self.assertEqual(razsiri("4A 3T 3A"), "AAAATTTAAA")
        self.assertEqual(razsiri(""), "")
        self.assertEqual(razsiri("1G 1C 1T 1A 1G"), "GCTAG")
        self.assertEqual(razsiri("14A 100G 2A 1C"), 14 * "A" + 100 * "G" + "AAC")


class Test02LZWStisni(unittest.TestCase):
    def test_lzw_stisni(self):
        self.assertEqual(
            lzw_stisni("DAVID", {"D": "110", "A": "01", "E": "00", "V": "111", "I": "10"}),
            "1100111110110")
        self.assertEqual(
            lzw_stisni("DADA", {"D": "110", "A": "01", "E": "00", "V": "111", "I": "10"}),
            "1100111001")
        self.assertEqual(
            lzw_stisni("XXX", {"D": "110", "A": "01", "E": "00", "X": "111", "I": "10"}),
            "111111111")
        self.assertEqual(
            lzw_stisni("", {"D": "110", "A": "01", "E": "00", "X": "111", "I": "10"}),
            "")
        self.assertEqual(
            lzw_stisni("X", {"D": "110", "A": "01", "E": "00", "X": "111", "I": "10"}),
            "111")

    def test_lzw_razsiri(self):
        self.assertEqual(
            lzw_razsiri("1100111110110", {"D": "110", "A": "01", "E": "00", "V": "111", "I": "10"}),
            "DAVID")
        self.assertEqual(
            lzw_razsiri("1100111001", {"D": "110", "A": "01", "E": "00", "V": "111", "I": "10"}),
            "DADA")
        self.assertEqual(
            lzw_razsiri("111111111", {"D": "110", "A": "01", "E": "00", "X": "111", "I": "10"}),
            "XXX")
        self.assertEqual(
            lzw_razsiri("", {"D": "110", "A": "01", "E": "00", "X": "111", "I": "10"}),
            "")
        self.assertEqual(
            lzw_razsiri("111", {"D": "110", "A": "01", "E": "00", "X": "111", "I": "10"}),
            "X")


class Test03OdkodirajZnak(unittest.TestCase):
    def test_odkodiraj(self):
        self.assertEqual(odkodiraj("110", [["E", "A"], ["I", ["D", "V"]]]), "D")
        self.assertEqual(odkodiraj("00", [["E", "A"], ["I", ["D", "V"]]]), "E")
        self.assertEqual(odkodiraj("01", [["E", "A"], ["I", ["D", "V"]]]), "A")
        self.assertEqual(odkodiraj("10", [["E", "A"], ["I", ["D", "V"]]]), "I")
        self.assertEqual(odkodiraj("111", [["E", "A"], ["I", ["D", "V"]]]), "V")

        self.assertEqual(odkodiraj("0", ["F", "G"]), "F")
        self.assertEqual(odkodiraj("1", ["F", "G"]), "G")


class Test04OdkodirajZnakR(unittest.TestCase):
    def test_odkodiraj(self):
        self.assertEqual(odkodiraj_rek("110", [["E", "A"], ["I", ["D", "V"]]]), "D")
        self.assertEqual(odkodiraj_rek("00", [["E", "A"], ["I", ["D", "V"]]]), "E")
        self.assertEqual(odkodiraj_rek("01", [["E", "A"], ["I", ["D", "V"]]]), "A")
        self.assertEqual(odkodiraj_rek("10", [["E", "A"], ["I", ["D", "V"]]]), "I")
        self.assertEqual(odkodiraj_rek("111", [["E", "A"], ["I", ["D", "V"]]]), "V")

        self.assertEqual(odkodiraj_rek("0", ["F", "G"]), "F")
        self.assertEqual(odkodiraj_rek("1", ["F", "G"]), "G")


class Test05Kodirnik(unittest.TestCase):
    def test_kodirnik(self):
        prepoved = Kodirnik()
        pepa = Kodirnik()

        self.assertEqual(prepoved.kode(), {})
        self.assertEqual(prepoved.znaki(), {})
        self.assertEqual(prepoved.kodirano(), [])

        prepoved.dodaj("P")

        self.assertEqual(prepoved.kode(), {"P": 0})
        self.assertEqual(prepoved.znaki(), {0: "P"})
        self.assertEqual(prepoved.kodirano(), [0])

        prepoved.dodaj("R")

        self.assertEqual(prepoved.kode(), {"P": 0, "R": 1})
        self.assertEqual(prepoved.znaki(), {0: "P", 1: "R"})
        self.assertEqual(prepoved.kodirano(), [0, 1])

        prepoved.dodaj("E")

        self.assertEqual(prepoved.kode(), {"P": 0, "R": 1, "E": 2})
        self.assertEqual(prepoved.znaki(), {0: "P", 1: "R", 2: "E"})
        self.assertEqual(prepoved.kodirano(), [0, 1, 2])

        prepoved.dodaj("P")

        self.assertEqual(prepoved.kode(), {"P": 0, "R": 1, "E": 2})
        self.assertEqual(prepoved.znaki(), {0: "P", 1: "R", 2: "E"})
        self.assertEqual(prepoved.kodirano(), [0, 1, 2, 0])

        prepoved.dodaj("O")

        self.assertEqual(prepoved.kode(), {"P": 0, "R": 1, "E": 2, "O": 3})
        self.assertEqual(prepoved.znaki(), {0: "P", 1: "R", 2: "E", 3: "O"})
        self.assertEqual(prepoved.kodirano(), [0, 1, 2, 0, 3])

        prepoved.dodaj("V")

        self.assertEqual(prepoved.kode(), {"P": 0, "R": 1, "E": 2, "O": 3, "V": 4})
        self.assertEqual(prepoved.znaki(), {0: "P", 1: "R", 2: "E", 3: "O", 4: "V"})
        self.assertEqual(prepoved.kodirano(), [0, 1, 2, 0, 3, 4])

        prepoved.dodaj("E")

        self.assertEqual(prepoved.kode(), {"P": 0, "R": 1, "E": 2, "O": 3, "V": 4})
        self.assertEqual(prepoved.znaki(), {0: "P", 1: "R", 2: "E", 3: "O", 4: "V"})
        self.assertEqual(prepoved.kodirano(), [0, 1, 2, 0, 3, 4, 2])

        prepoved.dodaj("D")

        self.assertEqual(prepoved.kode(), {"P": 0, "R": 1, "E": 2, "O": 3, "V": 4, "D": 5})
        self.assertEqual(prepoved.znaki(), {0: "P", 1: "R", 2: "E", 3: "O", 4: "V", 5: "D"})
        self.assertEqual(prepoved.kodirano(), [0, 1, 2, 0, 3, 4, 2, 5])

        self.assertEqual(pepa.kode(), {})
        self.assertEqual(pepa.znaki(), {})
        self.assertEqual(pepa.kodirano(), [])

        pepa.dodaj("P")
        pepa.dodaj("E")
        pepa.dodaj("P")
        pepa.dodaj("A")

        self.assertEqual(pepa.kode(), {"P": 0, "E": 1, "A": 2})
        self.assertEqual(pepa.znaki(), {0: "P", 1: "E", 2: "A"})
        self.assertEqual(pepa.kodirano(), [0, 1, 0, 2])

        self.assertEqual(prepoved.kode(), {"P": 0, "R": 1, "E": 2, "O": 3, "V": 4, "D": 5})
        self.assertEqual(prepoved.znaki(), {0: "P", 1: "R", 2: "E", 3: "O", 4: "V", 5: "D"})
        self.assertEqual(prepoved.kodirano(), [0, 1, 2, 0, 3, 4, 2, 5])


if __name__ == "__main__":
    unittest.main()
