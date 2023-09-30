from collections import defaultdict



def napredek(s):
    nazadovale,napredovale = 0,0
    letosnje = []
    for i in range(1,len(s) + 1):
        letosnje.append(i)
    for letos,prejsne in zip(letosnje,s):
        if letos < prejsne:
            napredovale += 1
        elif letos > prejsne:
            nazadovale += 1
    return (napredovale,nazadovale)


def clovek_ne_jezi_se(igralcev,meti):
    pozicije = [0] * igralcev
    igralec = 0
    for met in meti:
        nova = pozicije[igralec] + met
        pozicije = [0 if x == nova else x for x in pozicije]
        pozicije[igralec] = nova
        igralec += 1
        if igralec == igralcev:
            igralec = 0
    return pozicije


def zadnje_liho(s):
    if not s:
        return None
    if s[-1] % 2 == 1:
        return s[-1]
    return zadnje_liho(s[:-1])


def najvec_dve(s):
    pojavitve = defaultdict(int)
    i = 0
    while i < len(s):
        pojavitve[s[i]] += 1
        if pojavitve[s[i]] > 2:
            del s[i]
        else:
            i += 1


class Podjetje:

    def __init__(self, kapital):
        self.kapital = kapital

    def prejme(self, kapital1):
        self.kapital += kapital1

    def placa(self, kapital1, podjetje):
        podjetje.prejme(kapital1)
        self.kapital -= kapital1




import unittest
class Test01Olimpijske(unittest.TestCase):
    def test_olimpijske(self):
        self.assertEqual(napredek([1, 3, 2, 4, 6, 10, 7, 5, 9, 8]), (3, 3))
        self.assertEqual(napredek([5, 1, 2, 3, 4]), (1, 4))
        self.assertEqual(napredek([2, 3, 4, 5, 1]), (4, 1))
        self.assertEqual(napredek([1, 2, 3]), (0, 0))
        self.assertEqual(napredek([6, 2, 3, 4, 5, 1]), (1, 1))
        self.assertEqual(napredek([1, 2]), (0, 0))
        self.assertEqual(napredek([2, 1]), (1, 1))
        self.assertEqual(napredek([3, 2, 1]), (1, 1))
        self.assertEqual(napredek([1]), (0, 0))


class Test02ClovekNeJeziSe(unittest.TestCase):
    def test_clovek_ne_jezi_se(self):
        self.assertEqual(clovek_ne_jezi_se(2, [3, 1,
                                               3, 1,
                                               3, 1]), [9, 3])
        self.assertEqual(clovek_ne_jezi_se(2, [3, 1,
                                               3, 1,
                                               3]), [9, 2])
        self.assertEqual(clovek_ne_jezi_se(3, [3, 1, 2,
                                               1, 5]), [4, 6, 2])
        self.assertEqual(clovek_ne_jezi_se(2, [3, 3]), [0, 3])
        self.assertEqual(clovek_ne_jezi_se(2, [3, 2,
                                               3, 2,
                                               3, 5]), [0, 9])
        self.assertEqual(clovek_ne_jezi_se(2, [3, 2,
                                               3, 2,
                                               3, 5,
                                               1]), [1, 9])
        self.assertEqual(clovek_ne_jezi_se(5, [1, 2, 3, 4, 5,
                                               6, 6, 3, 5, 5]), [7, 8, 6, 9, 10])
        self.assertEqual(clovek_ne_jezi_se(5, [1, 2, 3, 4, 5,
                                               4, 3, 2, 1]), [0, 0, 0, 5, 0])
        self.assertEqual(clovek_ne_jezi_se(5, [1, 2, 3, 4, 5,
                                               4, 3, 2, 1, 1,
                                               2, 3]), [2, 3, 0, 5, 1])

class Test03ZadnjeLiho(unittest.TestCase):
    def test_zadnje_liho(self):
        try:
            zadnje_liho(list(range(0, 10000, 2)))
        except:
            pass
        else:
            self.fail("Funkcija mora biti rekurzivna")

        self.assertEqual(zadnje_liho([5]), 5)
        self.assertEqual(zadnje_liho([5, 1, 2, 3, 4]), 3)
        self.assertEqual(zadnje_liho([5, 2, 4, 6]), 5)
        self.assertEqual(zadnje_liho([5, 2, 4, 6]), 5)
        self.assertIsNone(zadnje_liho([2, 4, 6, 8]))
        self.assertEqual(zadnje_liho([2, 4, 6, 8, 1]), 1)
        self.assertEqual(zadnje_liho([2, 4, 6, 1, 8]), 1)
        self.assertEqual(zadnje_liho([2, 4, 1, 6, 8]), 1)
        self.assertEqual(zadnje_liho([2, 1, 4, 6, 8]), 1)
        self.assertEqual(zadnje_liho([1, 2, 4, 6, 8]), 1)
        self.assertEqual(zadnje_liho([2, 4, 6, 3, 8, 1]), 1)
        self.assertEqual(zadnje_liho([2, 3, 4, 6, 1, 8]), 1)
        self.assertEqual(zadnje_liho([3, 2, 4, 1, 6, 8]), 1)
        self.assertEqual(zadnje_liho([2, 3, 1, 4, 6, 8]), 1)
        self.assertEqual(zadnje_liho([1, 2, 4, 6, 8]), 1)
        self.assertEqual(zadnje_liho([1]), 1)
        self.assertIsNone(zadnje_liho([]))
        self.assertIsNone(zadnje_liho([4]))


class Test_04_NajvecDve(unittest.TestCase):
    def test_najvec_dve(self):
        s = [1, 2, 3, 4, 5, 6]
        self.assertIsNone(najvec_dve(s))
        self.assertEqual(s, [1, 2, 3, 4, 5, 6])

        s = [1, 2, 3, 1, 4, 5, 6]
        self.assertIsNone(najvec_dve(s))
        self.assertEqual(s, [1, 2, 3, 1, 4, 5, 6])

        s = [1, 2, 3, 1, 4, 5, 6, 1]
        self.assertIsNone(najvec_dve(s))
        self.assertEqual(s, [1, 2, 3, 1, 4, 5, 6])

        s = [1, 2, 3, 1, 4, 5, 6, 7, 6, 8, 6, 9, 1, 10]
        self.assertIsNone(najvec_dve(s))
        self.assertEqual(s, [1, 2, 3, 1, 4, 5, 6, 7, 6, 8, 9, 10])

        s = [1, 2, 3, 1, 4, 5, 6, 7, 1, 1, 1, 8, 1, 1, 8, 9]
        self.assertIsNone(najvec_dve(s))
        self.assertEqual(s, [1, 2, 3, 1, 4, 5, 6, 7, 8, 8, 9])

        s = [1, 1, 1, 1, 1]
        self.assertIsNone(najvec_dve(s))
        self.assertEqual(s, [1, 1])


class Test_05_Podjetje(unittest.TestCase):
    def test_podjetje(self):
        a = Podjetje(100)
        b = Podjetje(200)
        c = Podjetje(300)
        self.assertEqual(a.kapital, 100)
        self.assertEqual(b.kapital, 200)
        self.assertEqual(c.kapital, 300)

        a.prejme(50)
        self.assertEqual(a.kapital, 150)
        self.assertEqual(b.kapital, 200)
        self.assertEqual(c.kapital, 300)

        c.prejme(80)
        self.assertEqual(a.kapital, 150)
        self.assertEqual(b.kapital, 200)
        self.assertEqual(c.kapital, 380)

        c.placa(20, b)
        self.assertEqual(a.kapital, 150)
        self.assertEqual(b.kapital, 220)
        self.assertEqual(c.kapital, 360)

if __name__ == "__main__":
    unittest.main()