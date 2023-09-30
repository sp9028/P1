def v_zaporedje(signal):
    signal1 = signal.split()
    n = len(signal1) - 1
    i = 0
    while i <= n:
        if signal1[i] == "-":
            signal1.pop(i)
            signal1.insert(i, ".")
        elif signal1[i] == "---":
            signal1.pop(i)
            signal1.insert(i, "-")
        i += 1
    nov = signal.replace(' ', '?')
    nov6 = nov.replace("---","-")
    nov1 = nov6.replace("-?-","--")
    nov2 = nov1.replace("-?-","--")
    nov3 = nov2.replace("-???-", "-?-")
    nov4 = nov3.replace("-??????-", "-???-")
    i = 0
    presledek = []
    trojni_presledek = []

    while i < len(nov4):
        if nov4[i] == "?" and nov4[i + 1] == "-" and nov4[i - 1] == "-":
            index_1 = i
            presledek.append(index_1)
        elif nov4[i] == "?" and nov4[i + 1] == "?" and nov4[i + 2] == "?":
            index_3 = i
            trojni_presledek.append(index_3)
        i += 1
    i = 0
    while i < len(signal1):
        if i in presledek:
            signal1.insert(i," ")
        elif i in trojni_presledek:
            signal1.insert(i, " ")
            signal1.insert(i+1, " ")
            signal1.insert(i+1, " ")
        i += 1
    return "".join(signal1)


def vrni_znak(zaporedje,abeceda,morse):
    i = 0
    while i < len(morse):
        if zaporedje == morse[i]:
            return abeceda[i]
        i += 1


def v_besedo(zaporedje, abeceda, morse):
    i = 0
    beseda = []
    signal = zaporedje.split()
    while i < len(signal):
        crka = vrni_znak(signal[i],abeceda,morse)
        beseda.append(crka)
        i += 1
        rez = "".join(beseda)
    return rez


def v_znake(zaporedje, abeceda, morse):
    nov = zaporedje.replace("   ", " ? ")
    nov2 = nov.split('?')
    nov3 = " ".join(nov2).split(" ")
    trojni = []
    i = 0
    while i < len(nov3):
        if nov[i] == " ":
            trojni.append(i)
        i += 1
    signal = zaporedje.split("   ")
    nov1 = " ".join(signal)
    txt = (v_besedo(nov1,abeceda,morse))
    txt_list = list(txt)
    i = 0
    while i < len(txt_list):
        if i in trojni:
            txt_list.insert(i - 1 , " ")
        i += 1
    return "".join(txt_list)


def preberi(signal, abeceda, morse):
    return v_znake((v_zaporedje(signal)), abeceda, morse)


def zapisi(besedilo, abeceda, morse):
    i = 0
    besedilo1 = list(besedilo)
    abeceda1 = list(abeceda)
    indeksi = []
    while i < len(besedilo):
        if besedilo1[i] in abeceda1:
            index_crk = abeceda1.index(besedilo1[i])
            indeksi.append(index_crk)
        i += 1
    i = 0
    signal1 = []
    while i < len(indeksi):
        pravi_index = indeksi[i]
        signal = morse[pravi_index]
        signal1.append(signal)
        i += 1
    i = 0
    while i < len(besedilo1):
        if besedilo1[i] == " ":
            signal1.insert(i, "")
        i += 1
    spremenjen_signal = " ".join(signal1)
    signal2 = list(spremenjen_signal)
    spremenjen_signal2 = " ".join(signal2)
    originalen = spremenjen_signal2.replace("     ","      ")
    originalen1 = originalen.replace("-", "---")
    originalen2 = originalen1.replace(".", "-")
    return originalen2



import unittest
import random


class Test(unittest.TestCase):
    eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #           A      B       C      D      E     F      G        H      I
    eng_mor = ['.-', '-...', '-.-.', '--.', '.', '..-.', '--.', '....', '..',
               #             J      K       L     M     N      O      P       Q       R
               '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
               #             S    T     U      V       W       X       Y      Z
               '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

    slo = "ABCČDEFGHIJKLMNOPRSŠTUVZŽ"
    #           A      B       C       Č       D      E     F      G        H
    slo_mor = ['.-', '-...', '-.-.', '-.--.', '--.', '.', '..-.', '--.', '....',
               #            I     J      K       L     M     N      O      P        R
               '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',  '.-.',
               #             S     Š       T     U      V       W       X       Y
               '...', '---.-', '-', '..-', '...-', '.--', '-..-', '-.--',
               #             Z       Ž
               '--..', '--..-']


class TestObvezna(Test):
    def test_01_v_zaporedje(self):
        self.assertEqual(
            "..-. .-. ..   ..- .-..",
            v_zaporedje("- - --- -   - --- -   - -      - - ---   - --- - -"))

        self.assertEqual(
            "...- ... ---.-   ..-. .-. ..   ..- .-..",
            v_zaporedje("- - - ---   - - -   --- --- --- - ---      - - --- -   - --- -   - -      - - ---   - --- - -"))

    def test_02_vrni_znak(self):
        self.assertEqual("A", vrni_znak(".-", self.eng, self.eng_mor))
        self.assertEqual("Y", vrni_znak("-.--", self.eng, self.eng_mor))
        self.assertEqual("Č", vrni_znak("-.--.", self.slo, self.slo_mor))

        n = random.choice(self.eng)
        self.assertEqual(n, vrni_znak(".-", [n], [".-"]))

    def test_03_v_besedo(self):
        self.assertEqual("VSŠ",  v_besedo("...- ... ---.-", self.slo, self.slo_mor))
        self.assertEqual("FRI",  v_besedo("..-. .-. ..", self.slo, self.slo_mor))
        self.assertEqual("UL",  v_besedo("..- .-..", self.slo, self.slo_mor))

    def test_04_v_znake(self):
        self.assertEqual(
            "VSŠ FRI UL",
            v_znake("...- ... ---.-   ..-. .-. ..   ..- .-..", self.slo, self.slo_mor))

    def test_05_preberi(self):
        self.assertEqual(
            "VSŠ FRI UL",
            preberi("- - - ---   - - -   --- --- --- - ---      - - --- -   - --- -   - -      - - ---   - --- - -", self.slo, self.slo_mor))


class TestDodatna(Test):
    def test_zapisi(self):
        self.assertEqual(
            "- - - ---   - - -   --- --- --- - ---      - - --- -   - --- -   - -      - - ---   - --- - -",
            zapisi("VSŠ FRI UL", self.slo, self.slo_mor))


if __name__ == "__main__":
    unittest.main()



