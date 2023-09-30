from collections import defaultdict


def v_karanteno(aktivnosti, okuzene):
    karantena = set(okuzene)
    for oseba in aktivnosti:
        aktivnost = set(aktivnosti[oseba])
        for oseba1 in aktivnosti:
            if (oseba1 != oseba) and (oseba in okuzene or oseba1 in okuzene):
                aktivnost1 = set(aktivnosti[oseba1])
                if aktivnost & aktivnost1:
                    karantena.add(oseba)
                    karantena.add(oseba1)
    return karantena


def trojke(s,n):
    pogostosti = defaultdict(int)
    i = 0
    while i < len(s) - 2:
        pogostosti[s[i:i + 3]] += 1
        i += 1
        # Tako lahko damo ključ in vrednost v slovarju če iteriramo skozi items.
        # Values so pa samo vrednosti
    p = [(frek,trojka) for trojka,frek in pogostosti.items()]
    # Tako padajoče uredimo seznam
    p = sorted(p, reverse=True)
    return [trojka for (frek, trojka) in p[:n]]


def statistika(podatki, drzava, n):
    # Niz lahko splitamo po vrsticah z metodo splitlines ali split("\n")
    for vrstica in podatki.splitlines():
        d,o = vrstica.split(":")
        # Vzamem elemente od odzadaj je [-n:] zadnje n elementov
        if d == drzava:
            stevilke = [int(x) for x in o.split(",")]
            return sum(stevilke[-n:])
    return 0


def okuzeni(dan, prva, okuzbe):
    vsi = {prva}
    for oseba, kdaj in okuzbe[prva].items():
        if kdaj <= dan:
            vsi |= okuzeni(dan, oseba, okuzbe)
    return vsi


class Oseba:

    def __init__(self):
        self._vse_aktivnosti = set()

    def aktivnost(self, kaj, kdaj):
        self._vse_aktivnosti.add((kaj, kdaj))

    def vse_aktivnosti(self):
        # Če hočemo samo eno vrednostr v terki lahko za drugo damo _
        return {kaj for kaj,_ in self._vse_aktivnosti}

    def mozna_okuzba(self, druga_oseba):
        return self._vse_aktivnosti & druga_oseba._vse_aktivnosti != set()


class VarnaOseba(Oseba):

    def __init__(self, aktivnosti):
        super().__init__()
        self.aktivnosti = aktivnosti

    def mozna_okuzba(self, druga_oseba):
        return any(aktivnost[0] not in druga_oseba.aktivnosti
                   for aktivnost in self._vse_aktivnosti & druga_oseba._vse_aktivnosti)







import unittest

class Test(unittest.TestCase):
    def test_01_stiki(self):
        aktivnosti = {
            "Ana": ["kava", "trgovina", "kava", "burek"],
            "Berta": ["telovadba", "frizer"],
            "Cilka": ["telovadba"],
            "Dani": [],
            "Ema": ["kava", "telovadba"],
            "Fanči": ["frizer"],
            "Greta": ["lokostrelstvo", "kolesarjenje"]
        }
        self.assertEqual(
            {"Ana", "Berta", "Cilka", "Ema", "Fanči"},
            v_karanteno(aktivnosti, ["Ana", "Berta"]))
        self.assertEqual(
            {"Berta", "Cilka", "Ema", "Fanči"},
            v_karanteno(aktivnosti, ["Berta"]))
        self.assertEqual(
            {"Dani", "Greta"},
            v_karanteno(aktivnosti, ["Dani", "Greta"]))
        self.assertEqual(
            {"Dani"},
            v_karanteno(aktivnosti, ["Dani"]))
        self.assertEqual(
            {"Greta"},
            v_karanteno(aktivnosti, ["Greta"]))

    def test_02_pogoste_trojke(self):
        self.assertEqual(
            ['acg', 'tac', 'cga', 'gta', 'gat'],
            trojke("acgtacgatacgacg", 5)
        )

        self.assertEqual(
            ['acg', 'tac'],
            trojke("acgtacgatacgacg", 2)
        )

        self.assertEqual(
            ['cga', 'tcg', 'atc', 'gat', 'gtg'],
            trojke("acagtgcagcatcgatcgacatcgagtggggctacgatcgatcgatcgac", 5)
        )
        self.assertEqual(
            ['cga', 'acg', 'gac'],
            trojke("acgacgacgacga", 5)
        )
        self.assertEqual(
            ['cga', 'acg', 'gac'],
            trojke("acgacgacgacga", 5)
        )

        self.assertEqual(
            ['taa', 'aaa'],
            trojke('taaa', 2)
        )

        self.assertEqual(
            ['aaa', 'taa'],
            trojke('taaaa', 2)
        )

        spike = "tgtttgtttttcttgttttattgccactagtctctagtcagtgtgttaatcttacaaccagaactcaattaccccctgcatacactaattctttcacacgtggtgtttattaccctgacaaagttttcagatcctcagttttacattcaactcaggacttgttcttacctttcttttccaatgttacttggttccatgctatacatgtctctgggaccaatggtactaagaggtttgataaccctgtcctaccatttaatgatggtgtttattttgcttccactgagaagtctaacataataagaggctggatttttggtactactttagattcgaagacccagtccctacttattgttaataacgctactaatgttgttattaaagtctgtgaatttcaattttgtaatgatccatttttgggtgtttattaccacaaaaacaacaaaagttggatggaaagtgagttcagagtttattctagtgcgaataattgcacttttgaatatgtctctcagccttttcttatggaccttgaaggaaaacagggtaatttcaaaaatcttagggaatttgtgtttaagaatattgatggttattttaaaatatattctaagcacacgcctattaatttagtgcgtgatctccctcagggtttttcggctttagaaccattggtagatttgccaataggtattaacatcactaggtttcaaactttacttgctttacatagaagttatttgactcctggtgattcttcttcaggttggacagctggtgctgcagcttattatgtgggttatcttcaacctaggacttttctattaaaatataatgaaaatggaaccattacagatgctgtagactgtgcacttgaccctctctcagaaacaaagtgtacgttgaaatccttcactgtagaaaaaggaatctatcaaacttctaactttagagtccaaccaacagaatctattgttagatttcctaatattacaaacttgtgcccttttggtgaagtttttaacgccaccagatttgcatctgtttatgcttggaacaggaagagaatcagcaactgtgttgctgattattctgtcctatataattccgcatcattttccacttttaagtgttatggagtgtctcctactaaattaaatgatctctgctttactaatgtctatgcagattcatttgtaattagaggtgatgaagtcagacaaatcgctccagggcaaactggaaagattgctgattataattataaattaccagatgattttacaggctgcgttatagcttggaattctaacaatcttgattctaaggttggtggtaattataattacctgtatagattgtttaggaagtctaatctcaaaccttttgagagagatatttcaactgaaatctatcaggccggtagcacaccttgtaatggtgttgaaggttttaattgttactttcctttacaatcatatggtttccaacccactaatggtgttggttaccaaccatacagagtagtagtactttcttttgaacttctacatgcaccagcaactgtttgtggacctaaaaagtctactaatttggttaaaaacaaatgtgtcaatttcaacttcaatggtttaacaggcacaggtgttcttactgagtctaacaaaaagtttctgcctttccaacaatttggcagagacattgctgacactactgatgctgtccgtgatccacagacacttgagattcttgacattacaccatgttcttttggtggtgtcagtgttataacaccaggaacaaatacttctaaccaggttgctgttctttatcaggatgttaactgcacagaagtccctgttgctattcatgcagatcaacttactcctacttggcgtgtttattctacaggttctaatgtttttcaaacacgtgcaggctgtttaataggggctgaacatgtcaacaactcatatgagtgtgacatacccattggtgcaggtatatgcgctagttatcagactcagactaattctcctcggcgggcacgtagtgtagctagtcaatccatcattgcctacactatgtcacttggtgcagaaaattcagttgcttactctaataactctattgccatacccacaaattttactattagtgttaccacagaaattctaccagtgtctatgaccaagacatcagtagattgtacaatgtacatttgtggtgattcaactgaatgcagcaatcttttgttgcaatatggcagtttttgtacacaattaaaccgtgctttaactggaatagctgttgaacaagacaaaaacacccaagaagtttttgcacaagtcaaacaaatttacaaaacaccaccaattaaagattttggtggttttaatttttcacaaatattaccagatccatcaaaaccaagcaagaggtcatttattgaagatctacttttcaacaaagtgacacttgcagatgctggcttcatcaaacaatatggtgattgccttggtgatattgctgctagagacctcatttgtgcacaaaagtttaacggccttactgttttgccacctttgctcacagatgaaatgattgctcaatacacttctgcactgttagcgggtacaatcacttctggttggacctttggtgcaggtgctgcattacaaataccatttgctatgcaaatggcttataggtttaatggtattggagttacacagaatgttctctatgagaaccaaaaattgattgccaaccaatttaatagtgctattggcaaaattcaagactcactttcttccacagcaagtgcacttggaaaacttcaagatgtggtcaaccaaaatgcacaagctttaaacacgcttgttaaacaacttagctccaattttggtgcaatttcaagtgttttaaatgatatcctttcacgtcttgacaaagttgaggctgaagtgcaaattgataggttgatcacaggcagacttcaaagtttgcagacatatgtgactcaacaattaattagagctgcagaaatcagagcttctgctaatcttgctgctactaaaatgtcagagtgtgtacttggacaatcaaaaagagttgatttttgtggaaagggctatcatcttatgtccttccctcagtcagcacctcatggtgtagtcttcttgcatgtgacttatgtccctgcacaagaaaagaacttcacaactgctcctgccatttgtcatgatggaaaagcacactttcctcgtgaaggtgtctttgtttcaaatggcacacactggtttgtaacacaaaggaatttttatgaaccacaaatcattactacagacaacacatttgtgtctggtaactgtgatgttgtaataggaattgtcaacaacacagtttatgatcctttgcaacctgaattagactcattcaaggaggagttagataaatattttaagaatcatacatcaccagatgttgatttaggtgacatctctggcattaatgcttcagttgtaaacattcaaaaagaaattgaccgcctcaatgaggttgccaagaatttaaatgaatctctcatcgatctccaagaacttggaaagtatgagcagtatataaaatggccatggtacatttggctaggttttatagctggcttgattgccatagtaatggtgacaattatgctttgctgtatgaccagttgctgtagttgtctcaagggctgttgttcttgtggatcctgctgcaaatttgatgaagacgactctgagccagtgctcaaaggagtcaaattacattacacataa"
        self.assertEqual(
            ['ttt', 'att', 'ttg', 'aat', 'aaa'],
            trojke(spike, 5)
        )

        self.assertEqual(
            ['ttt', 'att', 'ttg', 'aat', 'aaa', 'tta', 'caa', 'aca'],
            trojke(spike, 8)
        )

    def test_03_statistika(self):
        podatki = """Slovenija:31,20,25,14,50,60
Hrvaška:150,170,200,220,221
Madžarska:100,70,35"""
        self.assertEqual(124, statistika(podatki, "Slovenija", 3))
        self.assertEqual(60, statistika(podatki, "Slovenija", 1))
        self.assertEqual(200, statistika(podatki, "Slovenija", 6))
        self.assertEqual(205, statistika(podatki, "Madžarska", 3))
        self.assertEqual(205, statistika(podatki, "Madžarska", 5))
        self.assertEqual(0, statistika(podatki, "Zanzibar", 5))

    def test_04_okuzeni(self):
        okuzbe = {
            "Ana": {"Berta": 6, "Cilka": 12, "Dani": 6},
            "Berta": {},
            "Cilka": {"Ema": 18, "Fanči": 30},
            "Dani": {"Greta": 9},
            "Ema": {"Helga": 24, "Iva": 36, "Jana": 27},
            "Fanči": {},
            "Greta": {"Klara": 12},
            "Helga": {},
            "Iva": {},
            "Jana": {},
            "Klara": {}
        }
        self.assertEqual(
            {"Ana", "Berta", "Cilka", "Dani", "Greta", "Klara"},
            okuzeni(15, "Ana", okuzbe))
        self.assertEqual(
            {"Ana", "Berta", "Dani"},
            okuzeni(6, "Ana", okuzbe))
        self.assertEqual(
            {"Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči", "Greta", "Helga", "Jana", "Klara"},
            okuzeni(30, "Ana", okuzbe))
        self.assertEqual(
            set(okuzbe),
            okuzeni(300, "Ana", okuzbe))
        self.assertEqual(
            {"Ana"},
            okuzeni(3, "Ana", okuzbe))

        self.assertEqual(
            {"Cilka", "Ema", "Helga"},
            okuzeni(26, "Cilka", okuzbe)
        )
        self.assertEqual(
            {"Cilka", "Ema", "Helga", "Jana"},
            okuzeni(28, "Cilka", okuzbe)
        )
        self.assertEqual(
            {"Cilka", "Ema", "Helga", "Jana"},
            okuzeni(27, "Cilka", okuzbe)
        )
        self.assertEqual(
            {"Dani", "Greta", "Klara"},
            okuzeni(30, "Dani", okuzbe)
        )
        self.assertEqual(
            {"Dani", "Greta"},
            okuzeni(10, "Dani", okuzbe)
        )

    def test_05_sledilnik_oseba(self):
        ana = Oseba()
        ana.aktivnost("kava", 15)
        ana.aktivnost("trgovina", 22)
        ana.aktivnost("kava", 25)
        self.assertEqual({"kava", "trgovina"}, ana.vse_aktivnosti())

        berta = Oseba()
        berta.aktivnost("kava", 12)
        berta.aktivnost("kava", 15)
        berta.aktivnost("frizer", 22)
        self.assertEqual({"kava", "frizer"}, berta.vse_aktivnosti())

        cilka = Oseba()
        cilka.aktivnost("trgovina", 25)
        cilka.aktivnost("frizer", 22)
        cilka.aktivnost("kava", 21)
        self.assertEqual({"kava", "trgovina", "frizer"}, cilka.vse_aktivnosti())

        self.assertTrue(ana.mozna_okuzba(berta))
        self.assertTrue(berta.mozna_okuzba(ana))

        self.assertTrue(cilka.mozna_okuzba(berta))
        self.assertTrue(berta.mozna_okuzba(cilka))

        self.assertFalse(ana.mozna_okuzba(cilka))
        self.assertFalse(cilka.mozna_okuzba(ana))

    def test_05_sledilnik_varna_oseba(self):
        ana = VarnaOseba({"trgovina", "frizer"})
        ana.aktivnost("kava", 15)
        ana.aktivnost("trgovina", 22)
        ana.aktivnost("kava", 25)
        self.assertEqual({"kava", "trgovina"}, ana.vse_aktivnosti())

        berta = VarnaOseba({"frizer"})
        berta.aktivnost("kava", 12)
        berta.aktivnost("kava", 25)
        berta.aktivnost("frizer", 22)
        self.assertEqual({"kava", "frizer"}, berta.vse_aktivnosti())

        cilka = VarnaOseba({"trgovina"})
        cilka.aktivnost("trgovina", 25)
        cilka.aktivnost("frizer", 22)
        cilka.aktivnost("kava", 21)
        self.assertEqual({"kava", "trgovina", "frizer"}, cilka.vse_aktivnosti())

        self.assertTrue(ana.mozna_okuzba(berta))
        self.assertTrue(berta.mozna_okuzba(ana))

        self.assertFalse(cilka.mozna_okuzba(berta))
        self.assertTrue(berta.mozna_okuzba(cilka))

        self.assertFalse(ana.mozna_okuzba(cilka))
        self.assertFalse(cilka.mozna_okuzba(ana))


if __name__ == "__main__":
    unittest.main()
