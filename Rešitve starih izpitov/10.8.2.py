class Figura:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ime = "Figura"

    def opis(self):
        return f"{self.ime} na {' abcdefgh'[self.x]}{self.y}"

    def premik(self, smer, razdalja):
        pass


class Trdnjava(Figura):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.ime = "Trdnjava"

    def premik(self, smer, razdalja):
        if smer == '|':
            self.y += razdalja
        elif smer == '-':
            self.x += razdalja


class Lovec(Figura):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.ime = "Lovec"

    def premik(self, smer, razdalja):
        if smer == "/":
            self.x += razdalja
            self.y += razdalja
        else:
            self.x -= razdalja
            self.y += razdalja



def koordinate_sosedov(x,y,teren):
    sosedi = set()
    sosedi |= {(x + 1,y), (x - 1, y), (x, y + 1), (x , y - 1)}
    if sosedi <= {(x,y) for y in range(len(teren)) for x in range(len(teren[0]))}:
        return sosedi
    else:
        sosedi = sosedi & {(x,y) for y in range(len(teren)) for x in range(len(teren[0]))}
    return sosedi


def vrhovi(teren):
    vrhovi = set()
    for y in range(len(teren)):
        for x in range(len(teren[0])):
            if len(koordinate_sosedov(x,y,teren)) == 4:
                for sx,sy in koordinate_sosedov(x,y,teren):
                    if teren[y][x] <= teren[sy][sx]:
                        break
                else:
                    vrhovi.add((x,y))
    return vrhovi


def najnizja(x,y, teren):
    naj = teren[y][x]
    for sx1,sy1 in koordinate_sosedov(x,y, teren):
        if teren[sy1][sx1] < teren[y][x]:
            naj_spodaj = najnizja(sx1,sy1, teren)
            if naj_spodaj < naj:
                naj = naj_spodaj
    return naj


def visinski_metri(pot, x, y, teren):
    visinci = 0
    visina = teren[y][x]
    for korak in pot:
        if korak == '<':
            x -= 1
        elif korak == '>':
            x += 1
        elif korak == "v":
            y += 1
        else:
            y -= 1
        nova_visina = teren[y][x]
        if nova_visina > visina:
            visinci += nova_visina - visina
        visina = nova_visina

    return visinci


def zretje(figure, poteze):
    figure = set(figure)
    for odkod,kam in poteze:
        figure.remove(odkod)
        figure.add(kam)
    return len(figure)






import unittest

class Test(unittest.TestCase):
    teren = ((6, 17, 18, 19, 21, 21),
             (8, 12, 3, 19, 23, 22),
             (14, 14, 13, 19, 20, 21),
             (15, 16, 12, 19, 23, 23),
             (9, 5, 11, 11, 25, 24),
             (8, 6, 8, 22, 22, 22),
             (8, 6, 8, 22, 22, 22))

    def test_1_koordinate_sosedov(self):
        teren = self.teren
        self.assertEqual(koordinate_sosedov(4, 2, teren), {(3, 2), (5, 2), (4, 1), (4, 3)})
        self.assertEqual(koordinate_sosedov(1, 2, teren), {(1, 1), (1, 3), (0, 2), (2, 2)})
        self.assertEqual(koordinate_sosedov(0, 2, teren), {(0, 1), (0, 3), (1, 2)})
        self.assertEqual(koordinate_sosedov(5, 2, teren), {(5, 1), (5, 3), (4, 2)})
        self.assertEqual(koordinate_sosedov(2, 0, teren), {(2, 1), (1, 0), (3, 0)})
        self.assertEqual(koordinate_sosedov(2, 6, teren), {(2, 5), (1, 6), (3, 6)})
        self.assertEqual(koordinate_sosedov(0, 0, teren), {(0, 1), (1, 0)})
        self.assertEqual(koordinate_sosedov(0, 6, teren), {(0, 5), (1, 6)})
        self.assertEqual(koordinate_sosedov(5, 0, teren), {(4, 0), (5, 1)})
        self.assertEqual(koordinate_sosedov(5, 6, teren), {(4, 6), (5, 5)})

    def test_1_vrhovi(self):
        self.assertEqual(vrhovi(self.teren), {(1, 3), (4, 1), (4, 4)})

    def test_2_najnizja(self):
        self.assertEqual(najnizja(4, 4, self.teren), 3)
        self.assertEqual(najnizja(3, 3, self.teren), 5)
        self.assertEqual(najnizja(4, 1, self.teren), 3)
        self.assertEqual(najnizja(2, 1, self.teren), 3)
        self.assertEqual(najnizja(2, 1, self.teren), 3)
        self.assertEqual(najnizja(3, 6, self.teren), 6)
        self.assertEqual(najnizja(0, 6, self.teren), 6)
        self.assertEqual(najnizja(5, 1, self.teren), 3)

    def test_3_visinski_metri(self):
        self.assertEqual(visinski_metri(">>>^<<", 1, 3, self.teren), 11)
        self.assertEqual(visinski_metri(">>>^<<^v", 1, 3, self.teren), 21)

    def test_4_zretje(self):
        self.assertEqual(
            zretje(("a2", "b1", "a6", "f3", "g5", "d8", "c3", "b4"),
                   [("a2", "a3"), ("a6", "b1"), ("a3", "b1"), ("c3", "c4"), ("f3", "c3")]),
                 #   premakne     požre         požre         premakne       premakne
            6)
        self.assertEqual(
            zretje(("a2", "b1"),
                   [("a2", "a3"), ("b1", "a2")]),
            2)
        self.assertEqual(
            zretje(("a2", "b1"),
                   [("a2", "b1")]),
            1)
        self.assertEqual(
            zretje(("a2", "b1"),
                   [("a2", "a3"), ("b1", "a3")]),
            1)

    def test_5_figure(self):
        t = Trdnjava(2, 5)
        self.assertEqual(t.opis(), "Trdnjava na b5")
        t.premik("|", 3)
        self.assertEqual(t.opis(), "Trdnjava na b8")
        t.premik("|", -2)
        self.assertEqual(t.opis(), "Trdnjava na b6")
        t.premik("-", 3)
        self.assertEqual(t.opis(), "Trdnjava na e6")
        t.premik("-", -1)
        self.assertEqual(t.opis(), "Trdnjava na d6")

        e = Lovec(1, 2)
        self.assertEqual(e.opis(), "Lovec na a2")
        e.premik("/", 4)
        self.assertEqual(e.opis(), "Lovec na e6")
        e.premik("\\", 2)
        self.assertEqual(e.opis(), "Lovec na c8")
        e.premik("\\", -3)
        self.assertEqual(e.opis(), "Lovec na f5")
        e.premik("/", 1)
        self.assertEqual(e.opis(), "Lovec na g6")


if __name__ == "__main__":
    unittest.main()
